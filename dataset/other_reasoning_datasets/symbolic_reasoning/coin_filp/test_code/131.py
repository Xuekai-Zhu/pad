def solution():
    coin = True
    people = {
        "Angel": True,
        "Sheryl": True,
        "Dulce": True,
        "Kenny": True
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