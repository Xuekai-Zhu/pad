def solution():
    coin = True
    people = {
        "Alonzo": False,
        "Dorothy": False,
        "Alfred": True,
        "Rodriguez": True
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