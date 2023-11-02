def solution():
    coin = True
    people = {
        "Maxwell": False,
        "Jose": True,
        "Beto": False,
        "Joe": False
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