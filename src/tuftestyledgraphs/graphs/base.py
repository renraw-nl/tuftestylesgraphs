from dataclasses import dataclass
from pathlib import Path
from typing import Any, Self

from matplotlib import pyplot as plt  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from matplotlib.figure import Figure  # type: ignore

from ..helpers import flag_first_in_loop
from ..stylesheets import BaseStyleSheet, TufteStyleSheet
from ..types import DataType, StyleType


@dataclass
class BaseGraph:
    """
    Base class for each type of graph, handles the shared basics.
    """

    stylesheet: BaseStyleSheet = None
    figsize: tuple[int] = None  # (16, 9)
    _ax: Axes = None
    _fig: Figure = None

    def __post_init__(self) -> None:
        """
        Reset the style details, and ensure there is an `Axes` object to plot
        to.
        """
        plt.close("all")

        if not self.stylesheet:
            self.stylesheet = TufteStyleSheet()

        # @TODO: This is a hack, but introduces style data into the
        # graph class.
        # Which should not be.
        overrides: StyleType = (
            self.style_overrides if hasattr(self, "style_overrides") else None
        )
        self.stylesheet.reset(overrides)

    def title(self, title: str) -> Self:
        plt.title(title)

    @property
    def ax(self) -> Axes:
        """
        Return `matplotlib`'s `Axes` object for the current Graph.

        This object was either passed during initiaion of the class, or
        created below.
        """
        if not self._ax:
            self._fig, self._ax = plt.subplots(figsize=self.figsize)

        return self._ax

    @property
    def fig(self) -> Figure:
        """
        Return `matplotlib`'s `Figure` object for the current Graph.

        This object was either passed during initiaion of the class, or
        created by `self.ax`.
        """
        if not self._fig:
            self._fig = self.ax.get_figure()

        return self._fig

    def rotate_xlabels(self, ratio: float = 0.8) -> Self:
        """
        Rotate the x-axis labels to `vertical` when the text width exceeds the
        ratio between text width and tick spacing.
        """
        tick_spacing = self.fig.get_figwidth() / float(
            len(self.ax.xaxis.get_majorticklocs())
        )
        font_size = [
            v.get_fontsize() for v in self.ax.xaxis.get_majorticklabels()
        ][0]
        FONT_RATE = 0.01
        char_width = font_size * FONT_RATE
        max_labelwidth = (
            max(len(v.get_text()) for v in self.ax.xaxis.get_majorticklabels())
            * char_width
        )

        if float(max_labelwidth) / tick_spacing >= ratio:
            plt.xticks(rotation=90)

        return self

    def draw(self) -> Self:
        """
        Create and show the graph.

        Also closes the plot to allow repeated calls without too much
        interference from previous calls.
        """
        plt.show()
        self.fig.tight_layout()
        self.fig.clear()
        plt.close(self.fig)

        return self

    def add(self, x: DataType, y: DataType, **kwargs: Any) -> Self:
        """Add a data set to plot"""
        raise NotImplementedError

    def show_values(
        self, fmt: str = "{: .1f}", padding: int = None, fontsize: int = None
    ) -> Self:
        """
        Show the values in the graph.

        For example, the values or label at the end of a line graph, or a
        bar graph.
        """
        raise NotImplementedError

    def save(self, to: Path) -> Self:
        """
        Save the graph to the provided file.
        """
        raise NotImplementedError

    def limit_spines(
        self, x_base: float | int = 1, y_base: float | int = 1
    ) -> Self:
        """
        Draw spines covering the data only.

        Optionally limit it to the ticks.
        """
        lns = self.ax.lines
        if len(lns) < 1:
            return self

        x_lim: tuple[float]
        y_lim: tuple[float]

        for ln, first in flag_first_in_loop(lns):
            if not ln:
                continue

            if first:
                x_lim = (ln.get_xdata().min(), ln.get_xdata().max())
                y_lim = (ln.get_ydata().min(), ln.get_ydata().max())
                continue

            x_lim = self.find_limits(x_lim, ln.get_xdata())
            y_lim = self.find_limits(y_lim, ln.get_ydata())

        x_lim = self.nearest_tick(x_lim, self.ax.get_xticks())
        y_lim = self.nearest_tick(y_lim, self.ax.get_yticks())

        sp = self.ax.spines
        sp.bottom.set_bounds(*x_lim)
        sp.bottom.set_visible(True)
        sp.left.set_bounds(*y_lim)
        sp.left.set_visible(True)

        return self

    def margins(self, x: float, y: float = None) -> Self:
        if y:
            self.ax.margins(x, y)
        else:
            self.ax.margins(x)

        return self

    @staticmethod
    def find_limits(
        lim: tuple[float | int, float | int],
        rng: tuple | list | dict,
    ) -> tuple[float, float]:
        """
        Find and return the smallest and largest values of the given range
        and existing limits.
        """
        return (min(lim[1], rng.min()), max(lim[0], rng.max()))

    @staticmethod
    def nearest_tick(
        lim: tuple[float | int, float | int],
        ticks: tuple | list | dict,
    ) -> tuple[float, float]:
        """
        Return the smallest and largest tick nearest to the given limits.
        """

        low = lim[0]
        for curr, first in flag_first_in_loop(ticks):
            if first:
                prev = curr
            elif prev <= low and low <= curr:
                low = prev  # if (low / (curr - prev)) <= 0.5 else curr
                break
            else:
                prev = curr

        high = lim[1]
        for curr, first in flag_first_in_loop(ticks[::-1]):
            if first:
                prev = curr
            elif curr <= high and high <= prev:
                high = prev  # if (high / (prev - curr)) <= 0.5 else prev
                break
            else:
                prev = curr

        return (
            low,
            high,
        )
