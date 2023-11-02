def solution():
    coin = True
    people = {
        "Rashad": False,
        "Savannah": True,
        "Flavio": False,
        "Bert": False
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