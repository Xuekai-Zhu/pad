def solution():
    coin = True
    people = {
        "Lizzy": True,
        "Juany": False,
        "Aisha": True,
        "Brenda": False
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