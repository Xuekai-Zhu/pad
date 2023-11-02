def solution():
    coin = True
    people = {
        "Glen": False,
        "Ariana": False,
        "Reggie": True,
        "Polo": True
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