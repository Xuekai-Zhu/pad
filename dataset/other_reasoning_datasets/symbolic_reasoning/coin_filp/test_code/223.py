def solution():
    coin = True
    people = {
        "Evan": False,
        "Ray": True,
        "Sofia": True,
        "Alonso": False
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