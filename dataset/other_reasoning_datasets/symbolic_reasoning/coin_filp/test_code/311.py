def solution():
    coin = True
    people = {
        "Thomas": True,
        "Cara": True,
        "Nita": False,
        "Frances": True
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