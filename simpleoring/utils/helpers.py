import numpy as np
from simpleoring.logging.logger import logger

check_negative_value_string = "ValueError: The value of the input parameter is not valid (should be positive)."
inner_outer_conflict_error_string = "The value of ID should be less than OD."

def check_negative_value(values):
    if any(v <= 0 for v in values):
        logger.error(check_negative_value_string)
        raise ValueError(check_negative_value_string)

def get_circular_oring_volume(CS: float, ID: float) -> float:
    check_negative_value([CS, ID])

    r = CS/2
    d = ID + r
    return np.pi**2 * r**2 * d

def get_oring_cord_volume(CS: float, L: float) -> float:
    check_negative_value([CS, L])
    r = CS/2
    a = np.pi*r**2
    return a * L

def get_circular_groove_volume(ID: float, OD: float, H: float) -> float:
    check_negative_value([ID, OD, H])
    if ID >= OD:
        logger.error(inner_outer_conflict_error_string)
        raise ValueError(inner_outer_conflict_error_string)

    r1 = ID/2
    r2 = OD/2
    a = np.pi * (r2**2 - r1**2)
    return a * H

def get_cord_groove_volume(ID: float, OD: float, H: float, L: float) -> float:
    check_negative_value([ID, OD, H, L])
    
    if ID >= OD:
        logger.error(inner_outer_conflict_error_string)
        raise ValueError(inner_outer_conflict_error_string)
    
    w = OD - ID
    a = w * H
    return a * L

def get_compression_ratio(CS: float, W: float) -> float:
    check_negative_value([CS, W])
    
    return (1 - CS/W) * 100

def get_compression(CS: float, W: float) -> float:
    check_negative_value([CS, W])    
    return (CS - W)

def get_inner_stretch(oring_id: float, groove_id: float) -> float:
    check_negative_value([oring_id, groove_id])

    oring_per = np.pi * oring_id
    groove_per = np.pi * groove_id
    return (oring_per - groove_per) / oring_per * 100

def get_outer_compression(oring_od: float, groove_od: float) -> float:
    check_negative_value([oring_od, groove_od])
    
    oring_per = np.pi * oring_od
    groove_per = np.pi * groove_od
    return -(oring_per - groove_per) / oring_per * 100

def get_house_fill_ratio(oring_volume: float, groove_volume: float) -> float:
    check_negative_value([oring_volume, groove_volume])
    
    return (oring_volume / groove_volume - 1) * 100