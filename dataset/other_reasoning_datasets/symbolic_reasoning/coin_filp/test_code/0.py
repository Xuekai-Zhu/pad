def solution():
    coin = True
    people = {
        "Breanna": True,
        "Trey": False,
        "Omar": True,
        "Patrice": False
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