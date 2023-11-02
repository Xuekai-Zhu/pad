def solution():
    coin = True
    people = {
        "Mercedes": False,
        "Adela": True,
        "Susana": True,
        "Rose": False
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