def solution():
    coin = True
    people = {
        "Donny": True,
        "Lucero": False,
        "Christopher": True,
        "Gregory": True
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