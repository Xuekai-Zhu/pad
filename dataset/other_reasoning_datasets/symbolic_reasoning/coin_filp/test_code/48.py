def solution():
    coin = True
    people = {
        "Craig": True,
        "Dillon": False,
        "Troy": False,
        "Griselda": False
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