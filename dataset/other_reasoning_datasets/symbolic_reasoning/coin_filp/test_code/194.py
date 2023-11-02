def solution():
    coin = True
    people = {
        "Virginia": False,
        "Juanita": False,
        "Zak": True,
        "Wayne": False
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