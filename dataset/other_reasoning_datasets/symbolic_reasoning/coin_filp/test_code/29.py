def solution():
    coin = True
    people = {
        "Geo": False,
        "Kody": False,
        "Isaias": True,
        "Giovanni": True
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