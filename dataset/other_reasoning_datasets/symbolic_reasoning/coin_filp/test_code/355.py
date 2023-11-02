def solution():
    coin = True
    people = {
        "Mia": False,
        "Art": False,
        "Samantha": True,
        "Lety": True
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