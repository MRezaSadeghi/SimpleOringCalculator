from simpleoring import condition, materials, properties
from simpleoring.mech import calc_helper

sealing_type = condition.Sealing.FaceSeal
cond = sealing_type.External

oring = properties.Oring(cross_section_dia=2.5, oring_id=95, material=materials.NBR70)
print(oring.oring_volume)
groove = properties.Groove(
    groove_depth=2.0, groove_id=97, groove_od=100, sealing_type=sealing_type
)
print(groove.groove_volume)

comp_ratio = calc_helper.get_characteristics(oring, groove, report=True)
calc_helper.evaluate_cond(oring, groove, cond)
