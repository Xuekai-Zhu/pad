def solution():
    coin = True
    people = {
        "Liz": False,
        "Andrea": True,
        "Suresh": False,
        "Vera": False
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