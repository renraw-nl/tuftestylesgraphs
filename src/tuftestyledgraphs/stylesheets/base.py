from dataclasses import dataclass
from typing import TypeVar

import matplotlib as mpl

StyleDict = TypeVar("StyleDict", bound=dict[str, str | bool | int | float])


@dataclass
class MatplotBaseStyleSheet:
    """
    A basic stylesheet based on `matplotlib`'s `rcParamsDefault`.
    """

    background: str = "white"
    colour: str = "black"
    fontsize: int = 10

    def reset(self, overrides: StyleDict = None):
        """
        Reset to default styles, then set those for Tufte-style graphs.

        It tries to find all defined `properties` ending in `_style`.
        """
        mpl.rcParams.update(mpl.rcParamsDefault)
        # plt.style.use(
        #   Path(__package__)) / 'var/rc/tufte.mplstyle'
        # )

        style_properties = dict()
        for p in dir(self.__class__):
            if isinstance(getattr(self.__class__, p), property) and p.endswith(
                "_style"
            ):
                style_properties = style_properties | getattr(self, p)

        if isinstance(overrides, StyleDict):
            style_properties = style_properties | overrides

        print(style_properties)

        mpl.rcParams.update(style_properties)
