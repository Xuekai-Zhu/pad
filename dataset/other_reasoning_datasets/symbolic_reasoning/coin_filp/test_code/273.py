def solution():
    coin = True
    people = {
        "Ace": True,
        "Rosy": False,
        "Kimberly": False,
        "Jean": False
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