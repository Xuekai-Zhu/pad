def solution():
    coin = True
    people = {
        "Tere": False,
        "Niko": True,
        "Keith": False,
        "Conner": False
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