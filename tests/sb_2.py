from simpleoring.mech.oring import Oring, FaceGroove, OringCalc
from simpleoring.mech import materials

my_oring = Oring(
    cross_section_dia=2,
    oring_id=10,
    oring_type="face_seal",
    oring_usage="external_pressure",
    material=materials.NBR70)

my_groove = FaceGroove(
    groove_id=10.1,
    groove_od=14,
    groove_depth=1.5)

calc = OringCalc()
calc._evaluate_face_seal(my_oring, my_groove)