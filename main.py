"""Main module of the API"""

from fastapi import FastAPI, HTTPException

from src.crud import create_hero, delete_hero, get_hero_by_id, get_heros, update_hero
from src.schemas import HeroSchemaIn

app = FastAPI()


@app.get("/", tags=["Hero"], summary="Return all heros")
def get_all():
    """
    Return all heros
    """

    try:
        heros = get_heros()

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400, detail="Error") from e

    return {"heros": heros}


@app.post("/", tags=["Hero"], summary="Create a new hero")
def post(item: HeroSchemaIn):
    """Create a new hero

    - **name**: the name of the hero
    - **classe** : the classe of the hero 'guerrier', 'mage', 'voleur', 'pretre'
    """

    try:
        hero = create_hero(**item.__dict__)

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400, detail="Error") from e

    return {"hero": hero}


@app.delete("/{hero_id}", tags=["Hero"], summary="Delete a hero by id")
def delete(hero_id: int):
    """Delete a hero by id"""

    try:
        hero = delete_hero(hero_id)

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400, detail="Error") from e

    return {"message": f"{hero.id_} deleted"}


@app.get("/{hero_id}", tags=["Hero"], summary="Return a hero by id")
def get_by_id(hero_id: int):
    """Return a hero by id"""

    try:
        hero = get_hero_by_id(hero_id)

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400, detail="Error") from e

    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")

    return {"hero": hero}


@app.put("/{hero_id}", tags=["Hero"], summary="Level up a hero by id")
def update(hero_id: int):
    """Level up a hero by id"""

    try:
        hero = update_hero(hero_id)

    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=400, detail="Error") from e

    return {"hero": f"{hero.name} level up to {hero.level} !"}
