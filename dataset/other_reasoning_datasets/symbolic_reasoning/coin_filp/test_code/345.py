def solution():
    coin = True
    people = {
        "Earl": True,
        "Rudy": False,
        "Harrison": True,
        "Nadine": False
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