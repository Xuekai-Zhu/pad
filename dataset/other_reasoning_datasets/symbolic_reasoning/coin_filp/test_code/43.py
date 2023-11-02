def solution():
    coin = True
    people = {
        "Lazaro": False,
        "Ana": True,
        "Charlotte": True,
        "Precious": True
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