def solution():
    coin = True
    people = {
        "Charmaine": False,
        "Vic": True,
        "Homero": True,
        "Jeanine": False
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