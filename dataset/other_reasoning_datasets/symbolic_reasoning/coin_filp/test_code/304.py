def solution():
    coin = True
    people = {
        "Marcus": True,
        "Ramirez": False,
        "Junior": True,
        "Arely": False
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