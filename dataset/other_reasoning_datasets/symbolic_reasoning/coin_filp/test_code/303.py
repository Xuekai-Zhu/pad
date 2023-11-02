def solution():
    coin = True
    people = {
        "Mabel": False,
        "Estela": True,
        "Irene": True,
        "May": True
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