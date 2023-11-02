def solution():
    coin = True
    people = {
        "Maura": True,
        "Selvin": False,
        "Tabitha": True,
        "Gino": True
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