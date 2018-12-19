# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW26.comp_surface_wind
SlotW26 Computation of winding surface method
@date Created on Mon Feb 22 12:11:27 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""

from numpy import arcsin, sin, pi


def comp_surface_wind(self):
    """Compute the Slot inner surface for winding (by analytical computation)

    Parameters
    ----------
    self : SlotW26
        A SlotW26 object

    Returns
    -------
    Swind: float
        Slot inner surface for winding [m**2]

    """

    # 2 half circle
    S1 = pi * self.R1 ** 2

    # Rectangle
    S2 = self.H1 * (2 * self.R1)

    # Height of the arc (P2,C1,P7)
    alpha2 = 2 * arcsin(self.W0 / (2.0 * self.R1))

    # Surface of arc (P2,C1,P7) in the isthmus
    Sarc = (self.R1 ** 2.0) / 2.0 * (alpha2 - sin(alpha2))

    return S1 + S2 - Sarc
