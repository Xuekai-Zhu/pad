def solution():
    coin = True
    people = {
        "Gavin": True,
        "Neha": False,
        "Asha": False,
        "Baltazar": False
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