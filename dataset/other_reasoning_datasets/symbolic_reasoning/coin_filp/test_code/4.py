def solution():
    coin = True
    people = {
        "Elise": True,
        "Lupe": True,
        "Renee": False,
        "Noemi": False
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