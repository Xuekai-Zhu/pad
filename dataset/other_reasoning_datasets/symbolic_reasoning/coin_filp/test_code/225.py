def solution():
    coin = True
    people = {
        "Les": False,
        "Jun": True,
        "Noe": True,
        "Juliana": True
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