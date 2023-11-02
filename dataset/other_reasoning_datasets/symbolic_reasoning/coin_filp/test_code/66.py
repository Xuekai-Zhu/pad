def solution():
    coin = True
    people = {
        "Angelique": True,
        "Marissa": True,
        "Phyllis": True,
        "Bonnie": True
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