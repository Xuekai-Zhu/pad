def solution():
    coin = True
    people = {
        "Jeff": False,
        "Jen": True,
        "Giselle": True,
        "Noel": False
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