def solution():
    coin = True
    people = {
        "Cassie": True,
        "Clifton": True,
        "Erik": False,
        "Everardo": False
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