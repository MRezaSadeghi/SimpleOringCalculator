from simpleoring import condition, materials, properties

# from simpleoring.logrecorder.logger import logger

oring = properties.Oring(cross_section_dia=2, oring_id=100, material=materials.NBR70)
groove = properties.Groove(groove_depth=2, groove_id=100, groove_od=110)
cond = condition.FaceSeal.Internal

print(cond.BACKUP_THRESHOLD_MPA.value)
