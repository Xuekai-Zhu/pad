def solution():
    coin = True
    people = {
        "Emely": True,
        "Chelsea": False,
        "Vladimir": True,
        "Tyrone": False
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