def solution():
    coin = True
    people = {
        "Cristina": True,
        "Saad": False,
        "Bridget": False,
        "Katie": True
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