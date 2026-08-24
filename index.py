from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Video Game Dictionary",
    description="A beginner-friendly REST API containing simple information about video games.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CAR DATA
vgames = [

    {
        "id": 1,
        "title": "Minecraft",
        "genre": "Sandbox",
        "year": 2011,
        "platform": "PC",
        "rating": 4.8,
        "description": "A sandbox game focused on exploration, building, crafting, and survival."
    },

    {
        "id": 2,
        "title": "Genshin Impact",
        "genre": "Action RPG",
        "year": 2020,
        "platform": "PC",
        "rating": 4.6,
        "description": "An open-world action RPG featuring exploration, combat, and elemental abilities."
    },

    {
        "id": 3,
        "title": "Call of Duty: Mobile",
        "genre": "First-Person Shooter",
        "year": 2019,
        "platform": "Mobile",
        "rating": 4.5,
        "description": "A mobile first-person shooter featuring multiplayer and battle royale modes."
    },

    {
        "id": 4,
        "title": "Wuthering Waves",
        "genre": "Action RPG",
        "year": 2024,
        "platform": "PC",
        "rating": 4.5,
        "description": "An open-world action RPG featuring exploration, fast-paced combat, and character-based gameplay."
    },

    {
        "id": 5,
        "title": "Left 4 Dead",
        "genre": "Survival Horror",
        "year": 2008,
        "platform": "PC",
        "rating": 4.7,
        "description": "A multiplayer first-person shooter where players fight through hordes of zombies."
    },

    {
        "id": 6,
        "title": "Fall Guys",
        "genre": "Battle Royale",
        "year": 2020,
        "platform": "PC",
        "rating": 4.4,
        "description": "A colorful multiplayer game where players compete in chaotic obstacle courses."
    }

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Video Game Dictionary!",
        "endpoints": [
            "/vgames",
            "/vgames/{id}",
            "/vgames/search"
        ]
    }


# GET ALL CARS
@app.get("/vgames")
def get_vgames():

    return {
        "count": len(vgames),
        "vgames": vgames
    }

# SEARCH CARS
@app.get("/vgames/search")
def search_vgames( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for games in vgames:
        searchable_text = (
            f"{games['title']} "
            f"{games['genre']} "
            f"{games['year']} "
            f"{games['platform']}"
        ).lower()

        if q in searchable_text:
            results.append(games)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }
    
# GET ONE CAR
@app.get("/vgames/{game_id}")
def get_game(game_id: int):

    for games in vgames:

        if games["id"] == game_id:
            return games

    raise HTTPException(
        status_code=404,
        detail="Game not found."
    )


