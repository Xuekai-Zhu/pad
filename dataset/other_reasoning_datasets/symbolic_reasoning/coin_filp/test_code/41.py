def solution():
    coin = True
    people = {
        "Pretty": True,
        "Jada": True,
        "Sarita": False,
        "Allen": True
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