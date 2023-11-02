def solution():
    coin = True
    people = {
        "Constance": True,
        "Nicholas": False,
        "Will": True,
        "Love": True
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