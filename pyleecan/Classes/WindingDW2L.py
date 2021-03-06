# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/WindingDW2L.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/WindingDW2L
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .WindingDW1L import WindingDW1L

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.WindingDW2L.get_dim_wind import get_dim_wind
except ImportError as error:
    get_dim_wind = error


from ._check import InitUnKnowClassError
from .Conductor import Conductor


class WindingDW2L(WindingDW1L):
    """double layer overlapping integral distributed winding, radial coil superposition"""

    VERSION = 1
    NAME = "double layer distributed"

    # cf Methods.Machine.WindingDW2L.get_dim_wind
    if isinstance(get_dim_wind, ImportError):
        get_dim_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use WindingDW2L method get_dim_wind: " + str(get_dim_wind)
                )
            )
        )
    else:
        get_dim_wind = get_dim_wind
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        coil_pitch=5,
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcpp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcpp" in list(init_dict.keys()):
                Npcpp = init_dict["Npcpp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
        # Set the properties (value check and convertion are done in setter)
        # Call WindingDW1L init
        super(WindingDW2L, self).__init__(
            coil_pitch=coil_pitch,
            is_reverse_wind=is_reverse_wind,
            Nslot_shift_wind=Nslot_shift_wind,
            qs=qs,
            Ntcoil=Ntcoil,
            Npcpp=Npcpp,
            type_connection=type_connection,
            p=p,
            Lewout=Lewout,
            conductor=conductor,
        )
        # The class is frozen (in WindingDW1L init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        WindingDW2L_str = ""
        # Get the properties inherited from WindingDW1L
        WindingDW2L_str += super(WindingDW2L, self).__str__()
        return WindingDW2L_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from WindingDW1L
        if not super(WindingDW2L, self).__eq__(other):
            return False
        return True

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from WindingDW1L
        S += super(WindingDW2L, self).__sizeof__()
        return S

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        # Get the properties inherited from WindingDW1L
        WindingDW2L_dict = super(WindingDW2L, self).as_dict()
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        WindingDW2L_dict["__class__"] = "WindingDW2L"
        return WindingDW2L_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from WindingDW1L
        super(WindingDW2L, self)._set_None()
