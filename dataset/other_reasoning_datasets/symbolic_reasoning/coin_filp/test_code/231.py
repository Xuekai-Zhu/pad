def solution():
    coin = True
    people = {
        "Roni": True,
        "Nikita": False,
        "Hannah": True,
        "Kiana": False
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