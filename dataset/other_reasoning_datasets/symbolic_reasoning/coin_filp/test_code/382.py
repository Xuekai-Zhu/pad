def solution():
    coin = True
    people = {
        "Cristal": True,
        "Roxana": True,
        "Rajesh": False,
        "Danny": False
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