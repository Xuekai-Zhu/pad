def solution():
    coin = True
    people = {
        "Raven": True,
        "Marisela": False,
        "Ross": True,
        "Angie": True
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