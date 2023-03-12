from dataclasses import dataclass
from pathlib import Path
from typing import Any, Self

from matplotlib import pyplot as plt  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from matplotlib.figure import Figure  # type: ignore

from ..stylesheets import BaseStyleSheet, TufteStyleSheet
from ..types import DataType, StyleType


@dataclass
class BaseGraph:
    """
    Base class for each type of graph, handles the shared basics.
    """

    title: str = None
    stylesheet: BaseStyleSheet = None
    figsize: tuple[int] = None  # (16, 9)
    _ax: Axes = None
    _fig: Figure = None

    def __post_init__(self) -> None:
        """
        Reset the style details, and ensure there is an `Axes` object to plot to.
        """
        if not self.stylesheet:
            self.stylesheet = TufteStyleSheet()

        # @TODO: This is a hack, but introduces style data into the graph class.
        # Which should not be.
        overrides: StyleType = (
            self.style_overrides if hasattr(self, "style_overrides") else None
        )
        self.stylesheet.reset(overrides)

    @property
    def ax(self) -> Axes:
        """
        Return `matplotlib`'s `Axes` object for the current Graph.

        This object was either passed during initiaion of the class, or created below.
        """
        if not self._ax:
            self._fig, self._ax = plt.subplots(figsize=self.figsize)

        return self._ax

    @property
    def fig(self) -> Figure:
        """
        Return `matplotlib`'s `Figure` object for the current Graph.

        This object was either passed during initiaion of the class, or created by
        `self.ax`.
        """
        if not self._fig:
            self._fig = self.ax.get_figure()

        return self._fig

    def rotate_xlabels(self, ratio: float = 0.8) -> Self:
        """
        Rotate the x-axis labels to `vertical` when the text width exceeds the ratio
        between text width and tick spacing.
        """
        tick_spacing = self.fig.get_figwidth() / float(
            len(self.ax.xaxis.get_majorticklocs())
        )
        font_size = [v.get_fontsize() for v in self.ax.xaxis.get_majorticklabels()][0]
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

        For example, the values or label at the end of a line graph, or a bar graph.
        """
        raise NotImplementedError

    def save(self, to: Path) -> Self:
        """
        Save the graph to the provided file.
        """
        raise NotImplementedError
