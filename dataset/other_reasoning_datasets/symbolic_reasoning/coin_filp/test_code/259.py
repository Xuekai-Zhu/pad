def solution():
    coin = True
    people = {
        "Nick": True,
        "Ada": True,
        "Stephany": False,
        "Suzie": True
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