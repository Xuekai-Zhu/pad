def solution():
    coin = True
    people = {
        "Annie": False,
        "Toño": True,
        "Sharon": True,
        "Delores": True
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