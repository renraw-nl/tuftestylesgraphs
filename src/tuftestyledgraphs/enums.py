from enum import StrEnum


class LineEnum(StrEnum):
    """
    Enum with matplotlib line styles

    Not used at the moment, unclear if needed.
    """

    SOLID: str = "-"
    DASHED: str = "--"
    DASHDOT: str = "-."
    DOTTED: str = ":"
    NONE: str = ""


class MarkerEnum(StrEnum):
    """
    Enum with matplotlib marker styles

    Not used at the moment, unclear if needed.
    """

    NONE: str = ""
    DOT: str = "o"
    POINT: str = "."
    X: str = "x"
    STAR: str = "*"
