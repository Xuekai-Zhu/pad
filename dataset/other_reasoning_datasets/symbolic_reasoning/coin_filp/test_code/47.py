def solution():
    coin = True
    people = {
        "Julieta": True,
        "Zachary": True,
        "Jared": True,
        "Tyson": False
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