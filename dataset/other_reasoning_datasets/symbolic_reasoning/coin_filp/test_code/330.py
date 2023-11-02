def solution():
    coin = True
    people = {
        "Sean": False,
        "Rebeca": True,
        "Marco": True,
        "Sami": True
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