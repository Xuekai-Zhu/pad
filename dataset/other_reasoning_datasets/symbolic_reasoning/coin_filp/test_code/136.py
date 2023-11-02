def solution():
    coin = True
    people = {
        "Connie": False,
        "Elena": False,
        "Tami": True,
        "Stuart": False
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