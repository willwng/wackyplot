"""
This file contains helper functions for plotting in a particular style
    to keep the plots consistent.

Note that each time you wish to make a plot, create a new PlotHelper object
"""
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import os

from plot_font_helper import *
from plot_style import PlotStyle


class PlotHelper:
    def __init__(self, style: PlotStyle, use_science: bool):
        self.ax = None
        self.ax_inset = None
        self.fig = None
        self.style = style
        if use_science:
            import scienceplots
            plt.style.use(['science', 'nature'])
        return

    def check_fig(self):
        """ Check if the figure exists """
        if self.fig is None:
            raise ValueError("No figure to save. Run get_axes() first.")
        return

    def add_common_xlabel(self, xlabel: str):
        """ Add a common x-label to the figure """
        self.check_fig()
        self.fig.supxlabel(xlabel, fontsize=get_common_label_size(self.style))

    def add_common_ylabel(self, ylabel: str):
        """ Add a common y-label to the figure """
        self.check_fig()
        self.fig.supylabel(ylabel, fontsize=get_common_label_size(self.style))

    def add_fig_title(self, title: str):
        """ Add a title to the figure """
        self.check_fig()
        self.fig.suptitle(title, fontsize=get_common_label_size(self.style))

    def set_ax_title(self, ax: plt.Axes, title: str):
        """ Set the title for the axes """
        assert ax in self.ax, f"Invalid axes: {ax}"
        ax.set_title(title, fontsize=get_axes_title_size(self.style))

    def set_ax_xlabel(self, ax: plt.Axes, xlabel: str):
        """ Set the x label for the axes """
        assert ax in self.ax, f"Invalid axes: {ax}"
        ax.set_xlabel(xlabel, fontsize=get_axes_label_size(self.style))

    def set_ax_ylabel(self, ax: plt.Axes, ylabel: str):
        """ Set the y label for the axes """
        assert ax in self.ax, f"Invalid axes: {ax}"
        ax.set_ylabel(ylabel, fontsize=get_axes_label_size(self.style))

    def set_tick_size(self):
        """ Set the tick size for the axes """
        self.check_fig()
        label_size = get_tick_size(self.style)
        # if axes is a list
        if isinstance(self.ax, np.ndarray):
            for ax in self.ax:
                ax.tick_params(axis='both', which='major',
                               labelsize=label_size)
                ax.tick_params(axis='both', which='minor',
                               labelsize=label_size)
        else:
            self.ax.tick_params(axis='both', which='major',
                                labelsize=label_size)
            self.ax.tick_params(axis='both', which='minor',
                                labelsize=label_size)

        # Set the tick size for the inset
        if self.ax_inset is not None:
            inset_label_size = get_tick_inset_size()
            self.ax_inset.tick_params(
                axis='both', which='major', labelsize=inset_label_size)
            self.ax_inset.tick_params(
                axis='both', which='minor', labelsize=inset_label_size)
        return

    def set_tick_middle_invisible(self):
        if self.style == PlotStyle.TWO_BY_TWO:
            # Remove all x-axis ticks except the bottom row
            for ax in self.ax[:-2]:
                ax.xaxis.set_tick_params(which='both', labelbottom=False)
            # Remove all y-axis ticks except the left column
            for ax in self.ax[1::2]:
                ax.yaxis.set_tick_params(which='both', labelleft=False)
        elif self.style == PlotStyle.TWO_BY_ONE:
            self.ax[1].yaxis.set_tick_params(which='both', labelleft=False)
        return

    def get_fig_axes(self) -> Tuple[plt.Figure, plt.Axes | np.ndarray[plt.Axes]]:
        """ Get the figure and axes for the given plot style """
        if self.style == PlotStyle.ONE_BY_ONE:
            fig, axes = plt.subplots(1, 1, figsize=(6, 5))
        elif self.style == PlotStyle.TWO_BY_ONE:
            fig, axes = plt.subplots(1, 2, figsize=(8, 4))
            axes = axes.flatten()
        elif self.style == PlotStyle.TWO_BY_TWO:
            fig, axes = plt.subplots(2, 2, figsize=(6, 5))
            axes = axes.flatten()
        else:
            raise ValueError(f"Invalid style: {self.style}")
        self.fig, self.ax = fig, axes
        # Post-generation
        self.set_tick_size()
        return fig, axes

    def add_inset(self):
        """ Add an inset to the figure """
        left, bottom, width, height = [0.6, 0.3, 0.3, 0.3]
        ax_inset = self.fig.add_axes([left, bottom, width, height])
        self.ax_inset = ax_inset
        return ax_inset

    def save_pdf_eps(self, filename: str):
        """ Save the figure as a PDF and EPS file """
        self.check_fig()
        self.fig.savefig(filename + ".pdf", dpi=600)
        self.fig.savefig(filename + ".eps", format="eps", dpi=600)
        return

    def save_pdf_trans(self, filename: str):
        """
        Save the figure as only a PDF (if transparency is needed)
        Use ghostscript to convert to EPS with transparency
        """
        self.check_fig()
        self.fig.savefig(filename + ".pdf", dpi=600)
        command = f"gs -q -dNOCACHE -dNOPAUSE -dBATCH -dSAFER -sDEVICE=eps2write -sOutputFile={filename}.eps {filename}.pdf"
        os.system(command)
        return
