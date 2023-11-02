def solution():
    coin = True
    people = {
        "Jim": True,
        "Dwayne": False,
        "Ricky": False,
        "Artemio": True
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