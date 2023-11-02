def solution():
    coin = True
    people = {
        "Emilia": True,
        "Jonas": True,
        "Christi": False,
        "Sophia": False
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