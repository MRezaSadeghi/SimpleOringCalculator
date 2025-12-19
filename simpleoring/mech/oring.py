from dataclasses import dataclass
from typing import Literal

from simpleoring.mech import calc_helper
from simpleoring.logging.logger import logger
from simpleoring.mech.materials import Material

oring_type = Literal["rod_seal", "piston_seal", "face_seal"]
oring_usage = Literal["static", "dynamic", "internal_pressure", "external_pressure"]

@dataclass
class Oring:
    cross_section_dia: float
    oring_id: float
    oring_type: oring_type
    oring_usage: oring_usage
    material: Material
    
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
        
@dataclass        
class FaceGroove:
    groove_id: float
    groove_od: float
    groove_depth: float
    
@dataclass        
class RodGroove: # for rod seal, groove on the cylinder
    pass
    
@dataclass        
class PistonGroove: # for piston seal, groove on the piston
    pass
    

class OringCalc:
    def __init__(self):
        pass
    
    def evaluate(self, oring: Oring, groove: FaceGroove|RodGroove|PistonGroove) -> None|bool:
        
        condition_couples = [("face_seal", FaceGroove), ("rod_seal", RodGroove), ("piston_seal", PistonGroove)]
        
        # oring/groove compatibility check
        for oring_type, groove_type in condition_couples:
            if oring.oring_type == oring_type and not isinstance(groove, groove_type):
                logger.critical(f"{oring_type} orings are only compatible for {oring_type} grooves")
                return None
        
        if oring.oring_type == "face_seal":
            self._evaluate_face_seal(oring, groove) 
        else:
            logger.critical("This part is under constuction, no Rod or Piston seal calculation is available")
            return None
        
    def _evaluate_face_seal(
        self,
        oring: Oring,
        groove: FaceGroove
        ) -> None|bool:

        groove_width = (groove.groove_od - groove.groove_id)/2
        
        compression_ratio = calc_helper.get_compression_ratio(
            CS = oring.cross_section_dia,
            W = groove.groove_depth
        )
        logger.debug(f"oring compression ratio (%): {compression_ratio:.1f}")
                
    def suggest_groove(
        self,
        oring: Oring,
        groove_boundaries: FaceGroove|RodGroove|PistonGroove
        ) -> FaceGroove|RodGroove|PistonGroove:
        pass