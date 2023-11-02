def solution():
    coin = True
    people = {
        "Bret": False,
        "Lois": True,
        "Ismael": True,
        "Mirna": True
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