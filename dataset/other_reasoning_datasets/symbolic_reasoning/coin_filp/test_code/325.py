def solution():
    coin = True
    people = {
        "Sabrina": True,
        "Pete": False,
        "Mary": False,
        "La": True
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