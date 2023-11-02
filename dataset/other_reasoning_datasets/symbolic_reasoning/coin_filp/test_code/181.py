def solution():
    coin = True
    people = {
        "Bobbi": False,
        "Tamika": False,
        "Zac": False,
        "Lala": True
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