from dataclasses import dataclass
from typing import Literal
from simpleoring.logging.logger import logger

oring_type = Literal["rod_seal", "piston_seal", "face_seal"]
oring_usage = Literal["static", "dynamic", "internal_pressure", "external_pressure"]

@dataclass
class Oring:
    cross_section_dia: float
    oring_id: float
    oring_type: oring_type
    oring_usage: oring_usage
    
    def __post_init__(self):
        if self.oring_type not in ("rod_seal", "piston_seal", "face_seal"):
            logger.error("invalid value for type")
            raise ValueError('type must be "rod_seal", "piston_seal", "face_seal"')
        
        if self.oring_usage not in ("static", "dynamic", "internal_pressure", "external_pressure"):
            logger.error("invalid value for usage")
            raise ValueError('usage must be "static", "dynamic", "internal_pressure", or "external_pressure"')
        
        if self.oring_type == "face_seal" and self.oring_usage in ("static", "dynamic"):
            _err_message = "face seal cannot be used in dynamic or static applications"
            logger.error(_err_message)
            raise ValueError(_err_message)
        
        if self.oring_type in ("rod_seal", "piston_seal") and self.oring_usage in ("internal_pressure", "external_pressure"):
            _err_message = "rod/piston seal cannot be used in internal/external pressure applications"
            logger.error(_err_message)
            raise ValueError(_err_message)