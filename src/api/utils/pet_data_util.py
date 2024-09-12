import random

def get_random_int(min: int, max: int) -> int:
    return random.randint(min, max)

pet_id = get_random_int(500, 10000)
pet = {
    "id": pet_id,
    "category": {
        "id": pet_id,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": pet_id,
            "name": "string"
        }
    ],
    "status": "available"
}