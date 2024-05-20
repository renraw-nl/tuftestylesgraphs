from typing import Self

from ..enums import StepEnum
from ..types import DataType
from .base import BaseGraph


class StepGraph(BaseGraph):
    """
    Create a Step graph.

    A bar type line graph:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html
    """

    def add(  # type: ignore
        self,
        x: DataType,
        y: DataType,
        colour: str = None,
        size: int = 12,
        where: StepEnum = StepEnum.PRE,
    ) -> Self:
        """
        Add a dataset to the graph
        """
        self.dots = self.ax.step(
            x,
            y,
            where=where,
            color=self.stylesheet.colour,
            **self.stylesheet.marker,
        )

        return self
