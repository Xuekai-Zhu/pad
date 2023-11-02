def solution():
    coin = True
    people = {
        "Evelyn": False,
        "Mason": False,
        "Shelby": False,
        "Aldo": True
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