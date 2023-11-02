def solution():
    coin = True
    people = {
        "Carla": True,
        "Dolores": True,
        "Cooper": True,
        "Damion": True
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