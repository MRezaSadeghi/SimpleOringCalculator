import numpy as np

from simpleoring import condition, materials, properties
from simpleoring.logrecorder.logger import logger
from simpleoring.mech import calc_helper

# choose the condition
sealing_type = condition.Sealing.RodSeal
cond = sealing_type.Static


# define the desired oring
oring = properties.Oring(cross_section_dia=1.6, oring_id=40, material=materials.NBR70)

# define the boundaries for the groove

g_depth = np.arange(1.2, 2.0, 0.05)
g_id = [40]
g_od = np.arange(41, 43, 0.05)


# Create all combinations and evaluate
results = []
for depth in g_depth:
    for od in g_od:
        for id_val in g_id:
            groove = properties.Groove(
                groove_depth=depth,
                groove_id=id_val,
                groove_od=od,
                sealing_type=sealing_type,
            )
            cost = calc_helper.evaluate_cond(oring, groove, cond, report=False)
            results.append((cost, depth, id_val, od))

# Find the minimum
best_cost, best_depth, best_id, best_od = min(results, key=lambda x: x[0])

logger.info(f"Best cost: {best_cost:.2f}")
logger.info(
    f"Best groove parameters: depth={best_depth:.2f}, id={best_id:.2f}, od={best_od:.2f}"
)

groove = properties.Groove(
    groove_depth=best_depth,
    groove_id=best_id,
    groove_od=best_od,
    sealing_type=sealing_type,
)
calc_helper.evaluate_cond(oring, groove, cond, report=True)
