from dataclasses import dataclass

from ..enums import MarkerEnum
from ..types import StyleType
from . import BaseStyleSheet


@dataclass
class TufteStyleSheet(BaseStyleSheet):
    """
    A `matplotlib` style sheet using Tufte's principles.
    """

    background: str = "#FFFFF8"
    colour: str = "#4B4B4B"
    fontsize: int = 10

    @property
    def figure_style(self) -> StyleType:
        """
        Provide basic figure styles
        """
        return {
            "text.color": self.colour,
            "axes.labelcolor": self.colour,
            "axes.edgecolor": self.colour,
            "axes.facecolor": self.background,
            "figure.facecolor": self.background,
            "figure.edgecolor": self.background,
            "figure.frameon": False,
            "figure.autolayout": True,
            "font.family": "serif",
            "font.size": self.fontsize,
            "font.style": "normal",
            "font.variant": "normal",
            "font.weight": "normal",
            "font.stretch": "normal",
        }

    @property
    def grid_style(self) -> StyleType:
        """
        Provide grid styles
        """
        return {
            "axes.grid": True,
            "axes.grid.axis": "x",
            "axes.grid.which": "major",
            "grid.color": self.background,
            "grid.linewidth": 1.0,
        }

    @property
    def axes_style(self) -> StyleType:
        """
        Provide axes styles
        """
        return {
            "xtick.color": self.colour,
            "ytick.color": self.colour,
            "xtick.bottom": False,
            "ytick.left": False,
        }

    @property
    def spines_style(self) -> StyleType:
        """
        Provide spine styles

        The lines around the graph, easily mixed with the axes lines.
        """
        return {
            "axes.spines.left": True,
            "axes.spines.bottom": True,
            "axes.spines.right": False,
            "axes.spines.top": False,
        }

    @property
    def marker(self) -> StyleType:
        """
        Set styles for a line marker.

        One with a little background filled edge to bring it out from the line.
        """
        return dict(
            marker=MarkerEnum.POINT,
            markersize=4**2,
            markerfacecolor=self.colour,
            # markerfacecoloralt='lightsteelblue',
            markeredgecolor=self.background,
            markeredgewidth=2.5,
        )
