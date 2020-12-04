# -*- coding: utf-8 -*-

from numpy import linspace, zeros

from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine


def get_surface_active(self, alpha=0, delta=0):
    """Return the full active surface

    Parameters
    ----------
    self : SlotM11
        A SlotM11 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_act: Surface
        Surface corresponding to the Active Area
    """

    # get the name of the lamination
    st = self.get_name_lam()

    [_, _, _, _, ZM1, ZM2, ZM3, ZM4] = self._comp_point_coordinate()
    curve_list = list()
    curve_list.append(Segment(ZM1, ZM2))
    if self.is_outwards():
        curve_list.append(
            Arc1(ZM2, ZM3, (Rbo + self.H0 - self.Hmag), is_trigo_direction=True)
        )
    else:
        curve_list.append(
            Arc1(ZM2, ZM3, (Rbo - self.H0 + self.Hmag), is_trigo_direction=True)
        )
    curve_list.append(Segment(ZM3, ZM4))
    if self.is_outwards():
        curve_list.append(Arc1(ZM4, ZM1, Rbo + self.H0, is_trigo_direction=True))
    else:
        curve_list.append(Arc1(ZM4, ZM1, Rbo - self.H0, is_trigo_direction=True))

    Zmid = (ZM1 + ZM3) / 2

    surface = SurfLine(
        line_list=curve_list, label="Wind_" + st + "_R0_T0_S0", point_ref=Zmid
    )

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface