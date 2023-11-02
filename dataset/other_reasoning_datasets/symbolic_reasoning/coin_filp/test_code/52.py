def solution():
    coin = True
    people = {
        "Irving": True,
        "Hans": True,
        "Moses": False,
        "Nicole": False
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