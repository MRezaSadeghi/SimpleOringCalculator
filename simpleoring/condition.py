from enum import Enum


class PistonSeal:
    class Static(Enum):
        SQUEEZE_MIN = 10.0
        SQUEEZE_MAX = 20.0
        SQUEEZE_OPT = 15.0
        GROOVE_FILL_MIN = 70.0
        GROOVE_FILL_MAX = 80.0
        STRETCH_MIN = 1.0
        STRETCH_MAX = 5.0
        RADIAL_COMPRESSION_MIN = 0.0
        RADIAL_COMPRESSION_MAX = 3.0
        BACKUP_THRESHOLD_MPA = 15.0

    class Reciprocating(Enum):
        SQUEEZE_MIN = 5.0
        SQUEEZE_MAX = 15.0
        SQUEEZE_OPT = 10.0
        GROOVE_FILL_MIN = 60.0
        GROOVE_FILL_MAX = 75.0
        STRETCH_MIN = 0.0
        STRETCH_MAX = 2.0
        RADIAL_COMPRESSION_MIN = 0.0
        RADIAL_COMPRESSION_MAX = 3.0
        BACKUP_THRESHOLD_MPA = 15.0

    class Rotary(Enum):
        SQUEEZE_MIN = 3.0
        SQUEEZE_MAX = 8.0
        SQUEEZE_OPT = 5.5
        GROOVE_FILL_MIN = 60.0
        GROOVE_FILL_MAX = 75.0
        STRETCH_MIN = 0.0
        STRETCH_MAX = 2.0
        RADIAL_COMPRESSION_MIN = None
        RADIAL_COMPRESSION_MAX = None
        BACKUP_THRESHOLD_MPA = 5.0


class RodSeal:
    class Static(Enum):
        SQUEEZE_MIN = 10.0
        SQUEEZE_MAX = 20.0
        SQUEEZE_OPT = 15.0
        GROOVE_FILL_MIN = 70.0
        GROOVE_FILL_MAX = 80.0
        STRETCH_MIN = 1.0
        STRETCH_MAX = 5.0
        RADIAL_COMPRESSION_MIN = 0.0
        RADIAL_COMPRESSION_MAX = 3.0
        BACKUP_THRESHOLD_MPA = 15.0

    class Reciprocating(Enum):
        SQUEEZE_MIN = 5.0
        SQUEEZE_MAX = 15.0
        SQUEEZE_OPT = 10.0
        GROOVE_FILL_MIN = 60.0
        GROOVE_FILL_MAX = 75.0
        STRETCH_MIN = 0.0
        STRETCH_MAX = 2.0
        RADIAL_COMPRESSION_MIN = 0.0
        RADIAL_COMPRESSION_MAX = 3.0
        BACKUP_THRESHOLD_MPA = 15.0

    class Rotary(Enum):
        SQUEEZE_MIN = 3.0
        SQUEEZE_MAX = 8.0
        SQUEEZE_OPT = 5.5
        GROOVE_FILL_MIN = 60.0
        GROOVE_FILL_MAX = 75.0
        STRETCH_MIN = 0.0
        STRETCH_MAX = 2.0
        RADIAL_COMPRESSION_MIN = None
        RADIAL_COMPRESSION_MAX = None
        BACKUP_THRESHOLD_MPA = 5.0


class FaceSeal:
    class Internal(Enum):
        SQUEEZE_MIN = 21.0
        SQUEEZE_MAX = 29.0
        SQUEEZE_OPT = 25.0
        GROOVE_FILL_MIN = 70.0
        GROOVE_FILL_MAX = 80.0
        STRETCH_MIN = 1.0
        STRETCH_MAX = 3.0
        RADIAL_COMPRESSION_MIN = None
        RADIAL_COMPRESSION_MAX = None
        BACKUP_THRESHOLD_MPA = 20.7

    class External(Enum):
        SQUEEZE_MIN = 21.0
        SQUEEZE_MAX = 29.0
        SQUEEZE_OPT = 25.0
        GROOVE_FILL_MIN = 70.0
        GROOVE_FILL_MAX = 80.0
        STRETCH_MIN = 0.0
        STRETCH_MAX = 0.0  # Not applicable
        RADIAL_COMPRESSION_MIN = 0.0
        RADIAL_COMPRESSION_MAX = 2.0
        BACKUP_THRESHOLD_MPA = 20.7
