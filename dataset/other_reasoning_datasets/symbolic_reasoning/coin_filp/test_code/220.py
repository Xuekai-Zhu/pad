def solution():
    coin = True
    people = {
        "Gus": False,
        "Brock": True,
        "Ava": False,
        "Jenna": True
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