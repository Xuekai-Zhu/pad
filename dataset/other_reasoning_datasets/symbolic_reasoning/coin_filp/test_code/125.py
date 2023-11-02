def solution():
    coin = True
    people = {
        "Rogelio": True,
        "Freddy": False,
        "Ivan": True,
        "Madeleine": False
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