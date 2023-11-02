def solution():
    coin = True
    people = {
        "Dana": False,
        "German": True,
        "Alvin": False,
        "Braden": True
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