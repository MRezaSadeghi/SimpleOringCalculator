import math
from dataclasses import dataclass

import numpy as np

from simpleoring.condition import Sealing
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
    sealing_type: Sealing.PistonSeal | Sealing.RodSeal | Sealing.FaceSeal

    def __post_init__(self):
        r1 = self.groove_id / 2
        r2 = self.groove_od / 2
        a = np.pi * (r2**2 - r1**2)
        self.groove_volume = a * self.groove_depth

        self.groove_char = None
        if self.sealing_type == Sealing.FaceSeal:
            self.groove_char = self.groove_depth
        else:
            self.groove_char = (self.groove_od - self.groove_id) / 2
