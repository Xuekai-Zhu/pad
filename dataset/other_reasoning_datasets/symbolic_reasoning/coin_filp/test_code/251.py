def solution():
    coin = True
    people = {
        "Angeles": True,
        "Richard": True,
        "Luciana": True,
        "Darlene": False
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