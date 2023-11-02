def solution():
    coin = True
    people = {
        "Dalila": True,
        "Emily": True,
        "Casey": False,
        "Clifford": False
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