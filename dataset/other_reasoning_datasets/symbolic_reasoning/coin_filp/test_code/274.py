def solution():
    coin = True
    people = {
        "Jeremy": False,
        "Simone": True,
        "Alondra": False,
        "Wyatt": False
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