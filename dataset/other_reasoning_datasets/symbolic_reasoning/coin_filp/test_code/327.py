def solution():
    coin = True
    people = {
        "Niki": True,
        "Graham": True,
        "Vernon": True,
        "Beau": True
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