def solution():
    coin = True
    people = {
        "Meg": False,
        "Andrey": False,
        "Gerard": True,
        "Lilia": True
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