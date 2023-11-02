def solution():
    coin = True
    people = {
        "Rosendo": True,
        "Shayla": False,
        "Erica": False,
        "Georgia": False
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