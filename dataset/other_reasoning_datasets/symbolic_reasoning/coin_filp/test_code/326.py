def solution():
    coin = True
    people = {
        "Estrella": False,
        "Madison": False,
        "Paco": False,
        "Rj": True
    }
    for person, flips in people.items():
        if flips:
            coin = not coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())