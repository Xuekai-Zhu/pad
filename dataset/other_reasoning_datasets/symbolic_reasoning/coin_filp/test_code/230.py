def solution():
    coin = True
    people = {
        "Leanne": True,
        "Lulu": False,
        "Lopez": False,
        "Jp": False
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