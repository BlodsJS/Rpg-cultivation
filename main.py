import random
summons = [
    "Humam",
    "Demon",
    "Dragon",
    "Angel",
    "Fishiman",
    "Half-Demon",
    "Half-Monster",
    "Spirit"
]
races = [
    {
        "race": "Humam",
        "atk": [1, 2, 3, 4, 5, 6],
        "vit": range(6)
    },
    {
        "race": "Demon"
    }
]

mobs = []
def spawn(entity: dict):
    for i in range(100000):
        name = random.choice(summons)
        entity = {
            "race": name,
            "atk": random.randint(3, 9),
            "vit": random.randint(3, 9),
            "agi": random.randint(3, 9)
        }
        mobs.append(entity)

spawn({})

print(mobs)
    
