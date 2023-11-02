def solution():
    coin = True
    people = {
        "Colton": True,
        "Dexter": False,
        "Katy": True,
        "Brayden": False
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