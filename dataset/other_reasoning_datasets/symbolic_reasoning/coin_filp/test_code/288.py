def solution():
    coin = True
    people = {
        "Luz": False,
        "Terence": True,
        "Elder": False,
        "Jazmin": False
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