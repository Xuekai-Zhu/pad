def solution():
    coin = True
    people = {
        "Clayton": False,
        "Edison": True,
        "Debbie": True,
        "Elvira": False
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