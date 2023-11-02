def solution():
    coin = True
    people = {
        "Chava": True,
        "Rosalia": False,
        "Kurt": False,
        "Linda": True
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