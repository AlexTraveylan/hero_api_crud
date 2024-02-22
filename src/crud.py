"""This module contains the CRUD functions for the Hero model"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models import Hero

engine = create_engine("sqlite:///database.db", echo=True)


def get_heros() -> list[Hero]:
    """Return all heros from the database

    Returns:
    --------
    list[Hero]
        The list of heros
    """
    with Session(engine) as connection:
        heros = connection.query(Hero).all()

    return heros


def get_hero_by_id(hero_id: int) -> Hero:
    """Return a hero by id from the database

    Parameters:
    -----------
    hero_id : int
        The id of the hero

    Returns:
    --------
    Hero
        The hero
    """
    with Session(engine) as connection:
        hero = connection.query(Hero).filter(Hero.id_ == hero_id).first()

    return hero


def create_hero(name: str, classe: str) -> Hero:
    """Create a new hero in the database

    Parameters:
    -----------
    name : str
        The name of the hero
    classe : str
        The classe of the hero "guerrier", "mage", "voleur", "pretre"

    Returns:
    --------
    Hero
        The hero created
    """

    with Session(engine) as connection:
        hero = Hero(name=name, classe=classe, level=1)
        connection.add(hero)
        connection.commit()
        connection.refresh(hero)

    return hero


def delete_hero(hero_id: int) -> Hero:
    """Delete a hero by id from the database

    Parameters:
    -----------
    hero_id : int
        The id of the hero

    Returns:
    --------
    Hero
        The hero deleted
    """
    with Session(engine) as connection:
        hero = connection.query(Hero).filter(Hero.id_ == hero_id).first()
        connection.delete(hero)
        connection.commit()

    return hero


def update_hero(hero_id: int) -> Hero:
    """hero level up

    Parameters:
    -----------
    hero_id : int
        The id of the hero

    Returns:
    --------
    Hero
        The hero updated
    """
    with Session(engine) as connection:
        hero = connection.query(Hero).filter(Hero.id_ == hero_id).first()
        hero.level += 1
        connection.commit()
        connection.refresh(hero)

    return hero
