def solution():
    coin = True
    people = {
        "Rosa": True,
        "Lana": True,
        "Curtis": False,
        "Rae": False
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