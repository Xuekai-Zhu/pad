def solution():
    coin = True
    people = {
        "Otto": False,
        "Marjorie": True,
        "Leonor": True,
        "Esther": True
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