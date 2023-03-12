from typing import Self

from . import BaseGraph
from ..types import DataType, StyleType


class HorizontalBarGraph(BaseGraph):
    """
    Create a Bar graph with the bars drawn horizontal.
    """

    def add(  # type: ignore
        self, x: DataType, y: DataType, colour: str = "lightgrey"
    ) -> Self:
        """
        Add a dataset to the graph
        """
        self.bars = self.ax.barh(x, y, color=colour, align="center")

        return self

    def show_values(
        self, fmt: str = "{: .1f}", padding: int = 3, fontsize: int = 8
    ) -> Self:
        """
        Add the column values to the edge of the bars
        """
        self.ax.bar_label(
            self.bars,
            fmt=fmt,
            label_type="edge",
            fontsize=fontsize,
            padding=padding,
        )

        return self


class VerticalBarGraph(HorizontalBarGraph):
    """
    Create a Bar graph with the bars drawn vertical.
    """

    @property
    def style_overrides(self) -> StyleType:
        """
        Add some specifics to the style sheet.

        @TODO: This needs to change.
        """
        return {
            "axes.grid.axis": "y",
        }

    def add(  # type: ignore
        self, x: DataType, y: DataType, colour: str = "lightgrey"
    ) -> Self:
        """
        Add a dataset to the graph
        """
        self.bars = self.ax.bar(
            x, y, color=colour if colour else self.stylesheet.colour, align="center"
        )

        return self
