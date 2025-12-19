from dataclasses import dataclass

@dataclass()
class Material:
    name: str
    elasticity: float
    shore_value: float

NBR70 = Material(name="NBR", elasticity=12e6, shore_value=70)
NBR90 = Material(name="NBR", elasticity=12e6, shore_value=90)
