from typing import Self

from .base import BaseGraph
from ..enums import MarkerEnum
from ..types import DataType, StyleType


class ScatterGraph(BaseGraph):
    """
    Create a Scatter graph.

    Essentially a line graph without the lines.
    """

    def add(  # type: ignore
        self, x: DataType, y: DataType, colour: str = None, size: int = 12
    ) -> Self:
        """
        Add a dataset to the graph
        """
        self.dots = self.ax.scatter(
            x,
            y,
            marker=MarkerEnum.POINT,
            s=size**2,
            edgecolor=self.stylesheet.background,
            facecolor=colour if colour else self.stylesheet.colour,
        )

        return self

    @property
    def style_overrides(self) -> StyleType:
        """Define additional styles which get set last."""
        return {
            "axes.grid": False,
            "grid.color": self.stylesheet.background,
            "xtick.color": self.stylesheet.colour,
            "ytick.color": self.stylesheet.colour,
            "xtick.bottom": True,
            "ytick.left": True,
        }
