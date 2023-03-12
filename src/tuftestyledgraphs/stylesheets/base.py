from dataclasses import dataclass

import matplotlib as mpl  # type: ignore

from ..helpers import flag_first_in_loop
from ..types import StyleType


@dataclass
class BaseStyleSheet:
    """
    A basic stylesheet based on `matplotlib`'s `rcParamsDefault`.
    """

    background: str = "white"
    colour: str = "black"
    fontsize: int = 10

    def reset(self, overrides: StyleType = None) -> None:
        """
        Reset to default styles, then set those for Tufte-style graphs.

        It tries to find all defined `properties` ending in `_style`.
        """
        mpl.rcParams.update(mpl.rcParamsDefault)
        # plt.style.use(
        #   Path(__package__)) / 'var/rc/tufte.mplstyle'
        # )

        style_properties: StyleType = dict()
        for p, first in flag_first_in_loop(dir(self)):
            if isinstance(getattr(self, p), dict) and p.endswith("_style"):
                if first:
                    style_properties = getattr(self, p)
                else:
                    style_properties = style_properties | getattr(self, p)

        if overrides:
            style_properties = style_properties | overrides

        mpl.rcParams.update(style_properties)
