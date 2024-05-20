from typing import Self

from ..types import DataType
from .base import BaseGraph


class LineGraph(BaseGraph):
    """
    Create a Line graph.

    Essentially a scatter graph with the lines.
    """

    def add(  # type: ignore
        self, x: DataType, y: DataType, colour: str = None, size: int = 12
    ) -> Self:
        """
        Add a dataset to the graph
        """
        self.dots = self.ax.plot(
            x,
            y,
            color=self.stylesheet.colour,
            **self.stylesheet.marker,
        )

        return self

    # @property
    # def style_overrides(self) -> StyleType:
    #     """Define additional styles which get set last."""
    #     return {
    #         "axes.grid": False,
    #         "grid.color": self.stylesheet.background,
    #         "xtick.color": self.stylesheet.colour,
    #         "ytick.color": self.stylesheet.colour,
    #         "xtick.bottom": True,
    #         "ytick.left": True,
    #     }
