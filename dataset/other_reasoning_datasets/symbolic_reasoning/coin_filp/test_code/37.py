def solution():
    coin = True
    people = {
        "Isela": True,
        "Leslie": True,
        "Stacy": True,
        "Ingrid": False
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