def solution():
    coin = True
    people = {
        "Carolyn": True,
        "Sasha": False,
        "Mercy": False,
        "Keri": True
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