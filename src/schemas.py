"""Module to define the schemas of the application"""

from pydantic import BaseModel, Field

from src.models import Classe


class HeroSchemaIn(BaseModel):
    """Schema of hero to create a new hero

    Attributes:
    -----------
    name : str
        The name of the hero
    classe : Classe
        The classe of the hero "guerrier", "mage", "voleur", "pretre"
    """

    name: str = Field(min_length=2, max_length=30)
    classe: Classe
