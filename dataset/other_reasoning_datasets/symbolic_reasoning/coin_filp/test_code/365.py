def solution():
    coin = True
    people = {
        "Trish": True,
        "Vero": True,
        "Victor": False,
        "Clemente": True
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