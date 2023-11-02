def solution():
    coin = True
    people = {
        "Sal": False,
        "Scott": True,
        "Myrna": True,
        "Maximo": True
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