GRAPH = {
    "user_id1": {"user_id2": 1, "user_id3": 1, "user_id4": 1},
    "user_id2": {"user_id1": 1, "user_id3": 1, "user_id5": 1, "user_id9": 1},
    "user_id3": {"user_id1": 1, "user_id2": 1, "user_id6": 1, "user_id8": 1, "user_id9": 1},
    "user_id4": {"user_id1": 1, "user_id5": 1, "user_id8": 1, "user_id9": 1},
    "user_id5": {"user_id4": 1, "user_id9": 1},
    "user_id6": {"user_id3": 1, "user_id7": 1, "user_id9": 1},
    "user_id7": {"user_id6": 1, "user_id8": 1, "user_id9": 1},
    "user_id8": {"user_id3": 1, "user_id4": 1, "user_id7": 1, "user_id9": 1},
    "user_id9": {
        "user_id2": 1,
        "user_id3": 1,
        "user_id4": 1,
        "user_id5": 1,
        "user_id6": 1,
        "user_id7": 1,
        "user_id8": 1,
        "user_id10": 1,
    },
    "user_id10": {"user_id9": 1},
}

HOBBIES = {
    "user_id1": "hiking",
    "user_id2": "running",
    "user_id3": "skiing",
    "user_id4": "climbing",
    "user_id5": "skiing",
    "user_id6": "climbing",
    "user_id7": "hiking",
    "user_id8": "hiking",
    "user_id9": "skiing",
    "user_id10": "running",
}

MUSIC = {
    "user_id1": "pop",
    "user_id2": "pop",
    "user_id3": "country",
    "user_id4": "alternative",
    "user_id5": "rock",
    "user_id6": "pop",
    "user_id7": "rock",
    "user_id8": "country",
    "user_id9": "pop",
    "user_id10": "rock",
}

MOVIES = {
    "user_id1": "comedy",
    "user_id2": "drama",
    "user_id3": "comedy",
    "user_id4": "sci-fi",
    "user_id5": "sci-fi",
    "user_id6": "drama",
    "user_id7": "drama",
    "user_id8": "comedy",
    "user_id9": "sci-fi",
    "user_id10": "comedy",
}
