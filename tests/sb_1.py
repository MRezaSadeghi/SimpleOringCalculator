from simpleoring import condition, materials, properties
from simpleoring.mech import calc_helper

sealing_type = condition.Sealing.RodSeal
cond = sealing_type.Static

oring = properties.Oring(cross_section_dia=1.6, oring_id=40, material=materials.NBR70)
print(oring.oring_volume)
groove = properties.Groove(
    groove_depth=1.6, groove_id=40, groove_od=43, sealing_type=sealing_type
)
print(groove)
print(oring)

comp_ratio = calc_helper.get_characteristics(oring, groove, report=True)
calc_helper.evaluate_cond(oring, groove, cond)
