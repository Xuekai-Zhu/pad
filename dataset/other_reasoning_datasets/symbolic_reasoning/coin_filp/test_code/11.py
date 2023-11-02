def solution():
    coin = True
    people = {
        "Christy": True,
        "Rey": False,
        "Michelle": True,
        "Dolly": False
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