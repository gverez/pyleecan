# -*- coding: utf-8 -*-
"""@package Methods.Machine.SlotW29.comp_surface
SlotW29 Computation of surface method
@date Created on Thu Feb 23 10:36:36 2017
@copyright (C) 2014-2015 EOMYS ENGINEERING.
@author pierre_b
"""

from numpy import sin


def comp_surface(self):
    """Compute the Slot total surface (by analytical computation).
    Caution, the bottom of the Slot is an Arc

    Parameters
    ----------
    self : SlotW29
        A SlotW29 object

    Returns
    -------
    S: float
        Slot total surface [m**2]

    """
    Rbo = self.get_Rbo()

    S0 = self.H0 * self.W0
    S1 = self.H1 * self.W1
    Swind = self.comp_surface_wind()

    # The bottom is an arc
    alpha = self.comp_angle_opening()
    Sarc = (Rbo ** 2.0) / 2.0 * (alpha - sin(alpha))

    # Because Slamination = S - Zs * Sslot
    if self.is_outwards():
        return S0 + S1 + Swind - Sarc
    else:
        return S0 + S1 + Swind + Sarc
