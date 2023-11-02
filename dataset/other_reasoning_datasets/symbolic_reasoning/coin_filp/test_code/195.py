def solution():
    coin = True
    people = {
        "Mari": True,
        "Ximena": True,
        "Leo": False,
        "Antonia": False
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