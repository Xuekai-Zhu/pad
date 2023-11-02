def solution():
    coin = True
    people = {
        "Conor": False,
        "Randall": False,
        "Oleg": True,
        "Stephanie": False
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