"""
This file contains helper functions for fonts to keep the plots consistent.
"""
from plot_style import PlotStyle


def get_common_label_size(style: PlotStyle) -> int:
    if style == PlotStyle.ONE_BY_ONE:
        return 22
    elif style == PlotStyle.TWO_BY_ONE:
        return 20
    elif style == PlotStyle.TWO_BY_TWO:
        return 18
    else:
        raise ValueError(f"Invalid style: {style}")


def get_axes_label_size(style: PlotStyle) -> int:
    if style == PlotStyle.ONE_BY_ONE:
        return 22
    elif style == PlotStyle.TWO_BY_ONE:
        return 20
    elif style == PlotStyle.TWO_BY_TWO:
        return 18
    else:
        raise ValueError(f"Invalid style: {style}")


def get_axes_title_size(style: PlotStyle) -> int:
    if style == PlotStyle.ONE_BY_ONE:
        return 18
    elif style == PlotStyle.TWO_BY_ONE:
        return 18
    elif style == PlotStyle.TWO_BY_TWO:
        return 18
    else:
        raise ValueError(f"Invalid style: {style}")


def get_tick_size(style: PlotStyle) -> int:
    if style == PlotStyle.ONE_BY_ONE:
        return 14
    elif style == PlotStyle.TWO_BY_ONE:
        return 14
    elif style == PlotStyle.TWO_BY_TWO:
        return 12
    else:
        raise ValueError(f"Invalid style: {style}")


def get_tick_inset_size() -> int:
    return 10
