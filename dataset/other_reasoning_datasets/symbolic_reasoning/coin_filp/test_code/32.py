def solution():
    coin = True
    people = {
        "Nubia": True,
        "Sarah": False,
        "Jalen": False,
        "Kris": True
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