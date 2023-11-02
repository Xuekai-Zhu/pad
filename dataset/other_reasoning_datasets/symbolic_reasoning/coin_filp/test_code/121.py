def solution():
    coin = True
    people = {
        "Arthur": True,
        "Shan": False,
        "Norman": True,
        "Manny": False
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