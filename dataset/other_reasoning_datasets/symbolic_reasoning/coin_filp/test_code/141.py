def solution():
    coin = True
    people = {
        "Eugenio": True,
        "Moises": False,
        "Marion": False,
        "Kirk": False
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