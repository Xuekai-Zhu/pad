def solution():
    coin = True
    people = {
        "Courtney": False,
        "Ann": True,
        "John": True,
        "Fer": True
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