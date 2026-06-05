import numpy as np

from simpleoring.condition import Sealing
from simpleoring.logrecorder.logger import logger
from simpleoring.properties import Groove, Oring


def check_boundary(
    value: float,
    value_name: str,
    min_val: float = None,
    max_val: float = None,
    report=True,
) -> bool:
    # Case: No boundaries defined
    if min_val is None and max_val is None:
        return 0

    # Check lower bound
    if min_val and value < min_val:
        if report:
            logger.warning(
                f"{value_name} should not be less than {min_val:.1f}, but it is {value:.1f}"
            )
        return abs(value - min_val)

    # Check upper bound
    if max_val and value > max_val:
        if report:
            logger.warning(
                f"{value_name} should not be higher than {max_val:.1f}, but it is {value:.1f}"
            )
        return abs(value - max_val)

    # Within bounds
    if min_val is not None and max_val is not None:
        if report:
            logger.info(f"{value_name} is in the boundary and works, it is {value:.1f}")
        return 0

    else:
        return 0


def get_housing_fill(oring: Oring, groove: Groove) -> float:
    logger.debug(f"housing vol: {(groove.groove_volume):.1f}mm")
    logger.debug(f"oring vol: {(oring.oring_volume):.1f}mm")
    return (oring.oring_volume / groove.groove_volume) * 100


def get_squeeze(oring: Oring, groove: Groove) -> float:
    logger.debug(f"compression: {(oring.cross_section_dia - groove.groove_char):.1f}mm")
    return -(groove.groove_char / oring.cross_section_dia - 1) * 100


def get_radial_stretch(oring: Oring, groove: Groove) -> float:
    # applicable for Piston seals, Internal pressure face seals
    return (groove.groove_id / oring.oring_id - 1) * 100


def get_radial_compression(oring: Oring, groove: Groove) -> float:
    # applicable for Rod seals, External pressure face seals
    return (1 - groove.groove_od / oring.oring_od) * 100


def get_characteristics(
    oring: Oring, groove: Groove, report=False
) -> tuple[float, float, float, float]:
    c1 = get_housing_fill(oring, groove)
    c2 = get_squeeze(oring, groove)
    c3 = get_radial_stretch(oring, groove)
    c4 = get_radial_compression(oring, groove)

    if report:
        logger.info(f"Housing fill (%): {c1:.2f}")
        logger.info(f"Compression (%): {c2:.2f}")
        logger.info(f"Rad. stretch (%): {c3:.2f}")
        logger.info(f"Rad. compression (%): {c4:.2f}")

    return c1, c2, c3, c4


def evaluate_cond(
    oring: Oring, groove: Groove, cond: Sealing.Values, report=False
) -> float:
    costs = []
    cost = check_boundary(
        get_housing_fill(oring, groove),
        "Housing fill",
        cond.GROOVE_FILL_MIN.value,
        cond.GROOVE_FILL_MAX.value,
        report=report,
    )
    costs.append(cost)

    cost = check_boundary(
        get_squeeze(oring, groove),
        "Squeeze",
        cond.SQUEEZE_MIN.value,
        cond.SQUEEZE_MAX.value,
        report=report,
    )
    costs.append(cost)

    cost = check_boundary(
        get_radial_stretch(oring, groove),
        "Rad. Stretch",
        cond.STRETCH_MIN.value,
        cond.STRETCH_MAX.value,
        report=report,
    )
    costs.append(cost)

    cost = check_boundary(
        get_radial_compression(oring, groove),
        "Rad. Compression",
        cond.RADIAL_COMPRESSION_MIN.value,
        cond.RADIAL_COMPRESSION_MAX.value,
        report=report,
    )
    costs.append(cost)
    c = np.sum(np.array(costs))

    logger.info(f"Overall Score: {-c:.1f}")

    return c
