def solution():
    coin = True
    people = {
        "Hayden": True,
        "Maya": False,
        "Zack": True,
        "Roberto": True
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