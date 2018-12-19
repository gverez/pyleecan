# -*- coding: utf-8 -*-
"""@package Methods.Geometry.Arc1.get_end
Return the end point of an Arc1 method
@date Created on Thu Jul 27 13:51:43 2018
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
@todo unittest it
"""


def get_end(self):
    """Return the end point of the arc

    Parameters
    ----------
    self : Arc1
        An Arc1 object

    Returns
    -------
    end: complex
        Complex coordinates of the end point of the Arc1
    """

    return self.end
