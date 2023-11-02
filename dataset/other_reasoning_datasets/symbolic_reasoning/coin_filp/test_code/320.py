def solution():
    coin = True
    people = {
        "Joyce": True,
        "Leroy": True,
        "Alyssa": False,
        "Maggie": False
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