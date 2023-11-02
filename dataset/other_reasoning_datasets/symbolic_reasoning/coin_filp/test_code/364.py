def solution():
    coin = True
    people = {
        "Drew": True,
        "Jhon": False,
        "Jayden": True,
        "Cliff": False
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