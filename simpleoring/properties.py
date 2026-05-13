import math
from dataclasses import dataclass

from simpleoring.materials import Material


@dataclass
class Oring:
    cross_section_dia: float
    oring_id: float
    material: Material

    def __post_init__(self):
        self.oring_od = self.oring_id + (2 * self.cross_section_dia)
        oring_rad = self.cross_section_dia / 2
        main_rad = self.oring_id + oring_rad
        self.oring_volume = 2 * math.pi**2 * main_rad * oring_rad**2


@dataclass
class Groove:
    groove_id: float
    groove_od: float
    groove_depth: float
