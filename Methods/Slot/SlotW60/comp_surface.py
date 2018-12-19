# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW60.comp_surface
SlotW60 Computation of surface method
@date Created on Wed Aug 01 10:22:33 2018
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import pi, arcsin, sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11] = self._comp_point_coordinate()
    Rext = self.get_Rbo()
    Rint = abs(Z5)

    # Surface of a slot pitch
    Sring = (pi * Rext ** 2 - pi * Rint ** 2) * 1 / self.Zs

    # Surface of the isocele triangle Z5 Z6 Z7
    D75 = abs(Z7 - Z5)
    Zmid = (Z5 + Z7) / 2
    H = abs(Z6 - Zmid)
    Stri = H * D75 / 2

    # Tooth surface
    St = self.H1 * self.W1 + self.H2 * self.W2

    alpha_top = 2 * arcsin(self.W1 / (2 * self.R1))
    Sarc_top = (self.R1 ** 2.0) / 2.0 * (alpha_top - sin(alpha_top))

    alpha_bot1 = 2 * arcsin(self.W2 / (2 * Rint))
    Sarc_bot1 = (Rint ** 2.0) / 2.0 * (alpha_bot1 - sin(alpha_bot1))

    alpha_bot2 = 2 * arcsin(D75 / (2 * Rint))
    Sarc_bot2 = (Rint ** 2.0) / 2.0 * (alpha_bot2 - sin(alpha_bot2))

    return Sring - (St + Sarc_top + Stri - Sarc_bot1 - Sarc_bot2)
