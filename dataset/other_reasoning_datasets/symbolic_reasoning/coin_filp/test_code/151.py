def solution():
    coin = True
    people = {
        "Kelvin": False,
        "Brennan": False,
        "Carina": True,
        "Paty": False
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