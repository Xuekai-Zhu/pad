def solution():
    coin = True
    people = {
        "Vicki": False,
        "Dwight": True,
        "Johnson": True,
        "Alexandra": True
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