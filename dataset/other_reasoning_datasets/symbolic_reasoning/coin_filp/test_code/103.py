def solution():
    coin = True
    people = {
        "Altagracia": True,
        "Howard": False,
        "Patti": True,
        "Douglas": True
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