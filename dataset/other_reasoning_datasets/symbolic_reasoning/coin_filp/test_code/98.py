def solution():
    coin = True
    people = {
        "Davis": True,
        "Jules": False,
        "Fabiola": True,
        "Cherie": False
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