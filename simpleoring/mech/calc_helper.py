import numpy as np

from simpleoring.condition import Sealing
from simpleoring.logrecorder.logger import logger
from simpleoring.properties import Groove, Oring


def check_boundary(
    value: float,
    value_name: str,
    min_val: float = None,
    max_val: float = None,
) -> bool:
    # Case: No boundaries defined
    if min_val is None and max_val is None:
        return 0

    # Check lower bound
    if min_val and value < min_val:
        logger.warning(
            f"{value_name} should not be less than {min_val:.1f}, but it is {value:.1f}"
        )
        return abs(value - min_val)

    # Check upper bound
    if max_val and value > max_val:
        logger.warning(
            f"{value_name} should not be higher than {max_val:.1f}, but it is {value:.1f}"
        )
        return abs(value - max_val)

    # Within bounds
    if min_val is not None and max_val is not None:
        logger.info(f"{value_name} is in the boundary and works, it is {value:.1f}")
        return 0

    else:
        print(min_val, max_val, value)
        return 0


def get_housing_fill(oring: Oring, groove: Groove) -> float:
    return -(groove.groove_volume / oring.oring_volume - 1) * 100


def get_squeeze(oring: Oring, groove: Groove) -> float:
    return -(groove.groove_char / oring.cross_section_dia - 1) * 100


def get_radial_stretch(oring: Oring, groove: Groove) -> float:
    # applicable for Piston seals, Internal pressure face seals
    return (groove.groove_id / oring.oring_id - 1) * 100


def get_radial_compression(oring: Oring, groove: Groove) -> float:
    # applicable for Rod seals, External pressure face seals
    return (oring.oring_od / groove.groove_od - 1) * 100


def get_characteristics(
    oring: Oring, groove: Groove, report=False
) -> tuple[float, float, float, float]:
    c1 = get_housing_fill(oring, groove)
    c2 = get_squeeze(oring, groove)
    c3 = get_radial_stretch(oring, groove)
    c4 = get_radial_compression(oring, groove)

    if report:
        logger.info(f"Housing fill (%): {c1:.1f}")
        logger.info(f"Squeeze (%): {c2:.1f}")
        logger.info(f"Rad. stretch (%): {c3:.1f}")
        logger.info(f"Rad. compression (%): {c4:.1f}")

    return c1, c2, c3, c4


def evaluate_cond(oring: Oring, groove: Groove, cond: Sealing.Values):
    costs = []
    cost = check_boundary(
        get_housing_fill(oring, groove),
        "Housing fill",
        cond.GROOVE_FILL_MIN.value,
        cond.GROOVE_FILL_MAX.value,
    )
    costs.append(cost)

    cost = check_boundary(
        get_squeeze(oring, groove),
        "Squeeze",
        cond.SQUEEZE_MIN.value,
        cond.STRETCH_MAX.value,
    )
    costs.append(cost)

    cost = check_boundary(
        get_radial_stretch(oring, groove),
        "Rad. Stretch",
        cond.STRETCH_MIN.value,
        cond.STRETCH_MAX.value,
    )
    costs.append(cost)

    cost = check_boundary(
        get_radial_compression(oring, groove),
        "Rad. Compression",
        cond.RADIAL_COMPRESSION_MIN.value,
        cond.RADIAL_COMPRESSION_MAX.value,
    )
    costs.append(cost)
    c = np.sum(np.array(costs))

    logger.info(f"Overall Cost: {c:.1f}")


"""
exit()

check_negative_value_string = (
    "ValueError: The value of the input parameter is not valid (should be positive)."
)
inner_outer_conflict_error_string = "The value of ID should be less than OD."


def check_negative_value(values):
    if any(v <= 0 for v in values):
        logger.error(check_negative_value_string)
        raise ValueError(check_negative_value_string)


def get_circular_oring_volume(CS: float, ID: float) -> float:
    check_negative_value([CS, ID])

    r = CS / 2
    d = ID + r
    return np.pi**2 * r**2 * d


def get_oring_cord_volume(CS: float, L: float) -> float:
    check_negative_value([CS, L])
    r = CS / 2
    a = np.pi * r**2
    return a * L


def get_circular_groove_volume(ID: float, OD: float, H: float) -> float:
    check_negative_value([ID, OD, H])
    if ID >= OD:
        logger.error(inner_outer_conflict_error_string)
        raise ValueError(inner_outer_conflict_error_string)

    r1 = ID / 2
    r2 = OD / 2
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

    return (1 - W / CS) * 100


def get_compression(CS: float, W: float) -> float:
    check_negative_value([CS, W])
    return CS - W


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
"""
