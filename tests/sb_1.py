from simpleoring import condition, materials, properties
from simpleoring.mech import calc_helper

sealing_type = condition.Sealing.FaceSeal
cond = sealing_type.Internal

oring = properties.Oring(cross_section_dia=2, oring_id=70, material=materials.NBR70)
print(oring.oring_volume)
groove = properties.Groove(
    groove_depth=1.6, groove_id=69.9, groove_od=74.0, sealing_type=sealing_type
)
print(groove)
print(oring)

comp_ratio = calc_helper.get_characteristics(oring, groove, report=True)
calc_helper.evaluate_cond(oring, groove, cond)
