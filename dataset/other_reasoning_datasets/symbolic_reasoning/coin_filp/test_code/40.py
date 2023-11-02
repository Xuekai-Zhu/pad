def solution():
    coin = True
    people = {
        "Jr": True,
        "Meredith": True,
        "Zoe": False,
        "Robby": False
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