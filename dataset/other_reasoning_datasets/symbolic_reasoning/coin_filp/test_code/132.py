def solution():
    coin = True
    people = {
        "Selina": True,
        "Tasha": True,
        "Jarrod": False,
        "Maddy": False
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