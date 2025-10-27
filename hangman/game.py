def init_state(secret: str, max_tries: int):
    return {
        "secret": str,  # הלימה תידוסה
        "display": list[str],  # תמישר םיוות הגוצתל , "_"
        "guessed": set[str],  # תויתוא ושחונש
        "wrong_guesses": int,  # המכ תויועט ועצוב
        "max_tries": int}  # הלבג}


def validate_guess(ch: str, guessed: set[str]):
    return tuple[bool, str]


def apply_guess(state: dict, ch: str):
    return bool


def is_won(state: dict):
    return bool


def is_lost(state: dict):
    return bool


def render_display(state: dict):
    return str


def render_summary(state: dict):
    return str
