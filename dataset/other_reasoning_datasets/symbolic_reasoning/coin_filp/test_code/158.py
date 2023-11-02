def solution():
    coin = True
    people = {
        "Peggy": True,
        "Trent": True,
        "Darrell": True,
        "Pamela": True
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