# -*- coding: utf-8 -*-
"""@package Methods.Machine.VentilationPolar.check
Check the ventilation parameters methods
@date Created on Wed Mar 07 17:33:33 2015
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def check(self):
    """Make sure that the ventilation parameters are correctly set

    Parameters
    ----------
    self : VentilationPolar
        A VentilationPolar object

    Returns
    -------
    None

    Raises
    _______
    VentilationPolarInstanceError
        Zh must be a integer
        H0 must be a float or int
        D0 must be a float or int
        Alpha0 must be a float or int
    """

    if not isinstance(self.Zh, int):
        raise VentilationPolarInstanceError("Zh must be a integer")
    if not isinstance(self.H0, float) and not isinstance(self.H0, int):
        raise VentilationPolarInstanceError("H0 must be a float or int")
    if not isinstance(self.D0, float) and not isinstance(self.D0, int):
        raise VentilationPolarInstanceError("D0 must be a float or int")
    if not isinstance(self.Alpha0, float) and not isinstance(self.Alpha0, int):
        raise VentilationPolarInstanceError("Alpha0 must be a float or int")


class VentilationPolarInstanceError(Exception):
    """ """

    pass
