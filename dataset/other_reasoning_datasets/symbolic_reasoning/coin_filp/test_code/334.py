def solution():
    coin = True
    people = {
        "Kristen": True,
        "Herbert": True,
        "Benny": False,
        "El": False
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