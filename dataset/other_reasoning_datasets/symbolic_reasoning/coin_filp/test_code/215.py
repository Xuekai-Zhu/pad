def solution():
    coin = True
    people = {
        "Adalberto": True,
        "Jamal": False,
        "Carter": True,
        "Robyn": False
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