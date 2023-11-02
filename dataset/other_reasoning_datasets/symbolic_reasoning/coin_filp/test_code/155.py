def solution():
    coin = True
    people = {
        "Guillermo": False,
        "Gerry": False,
        "Lizbeth": True,
        "Charly": True
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