def solution():
    coin = True
    people = {
        "Abel": True,
        "Mallory": True,
        "Theresa": False,
        "Quinn": True
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