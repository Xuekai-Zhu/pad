def solution():
    coin = True
    people = {
        "Sherry": False,
        "Ben": True,
        "Allison": False,
        "Anthony": True
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