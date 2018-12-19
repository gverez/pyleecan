# -*- coding: utf-8 -*-
"""@package Methods.Machine.Magnet_Type_2.build_geometry
Magnet_Type_2 build_geometry method
@date Created on Wed Dec 17 16:09:15 2014
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import array, exp, arctan

from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment, Arc1) needed to plot the Magnet.
    The list represents a closed surface.
    The ending point of a curve is always the starting point of the next curve
    in the list

    Parameters
    ----------
    self : Magnet_Type_11
        A Magnet_Type_11 object
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_simplified: bool
        True to avoid line superposition

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the magnet

    """

    # defining label for type_magnetization
    if self.type_magnetization == 0:
        t_p = "Radial"
    else:
        t_p = "Parallel"

    [Z1, Z2, Z3, Zs3, Zs4, Z4, Zref] = self._comp_point_coordinate()
    # Creation of curve
    curve_list = list()
    if is_simplified and W0 > self.Wmag:
        curve_list.append(Segment(Z1, Z3))
    elif is_simplified and H0 < self.Hmag:
        curve_list.append(Segment(Zs3, Z3))
    elif not is_simplified:
        curve_list.append(Segment(Z1, Z3))

    curve_list.append(Arc1(Z3, Z4, abs(Z3)))

    if is_simplified and W0 > self.Wmag:
        curve_list.append(Segment(Z4, Z2))
    elif is_simplified and H0 < self.Hmag:
        curve_list.append(Segment(Z4, Zs4))
    elif not is_simplified:
        curve_list.append(Segment(Z4, Z2))

    if not is_simplified:
        curve_list.append(Arc1(Z2, Z1, -abs(Z2)))

    surf_list = list()
    surf_list.append(
        SurfLine(
            line_list=curve_list,
            label="MagnetRotor" + t_p + "_N_R0_T0_S0",
            point_ref=Zref,
        )
    )

    # Apply transformation
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list
