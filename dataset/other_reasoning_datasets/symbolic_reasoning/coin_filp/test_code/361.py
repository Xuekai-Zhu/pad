def solution():
    coin = True
    people = {
        "María": True,
        "Fredy": True,
        "Bridgette": True,
        "Kenya": False
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