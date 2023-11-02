def solution():
    coin = True
    people = {
        "Dino": True,
        "Toby": False,
        "Abigail": True,
        "Manuela": False
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