def solution():
    coin = True
    people = {
        "Norma": False,
        "Timothy": True,
        "Willie": False,
        "Mathew": False
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