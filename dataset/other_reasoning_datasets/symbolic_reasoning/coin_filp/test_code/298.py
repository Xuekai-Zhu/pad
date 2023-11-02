def solution():
    coin = True
    people = {
        "Mario": True,
        "Pierre": False,
        "Amit": True,
        "Nelson": False
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