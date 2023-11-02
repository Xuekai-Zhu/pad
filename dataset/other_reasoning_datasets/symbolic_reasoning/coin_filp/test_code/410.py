def solution():
    coin = True
    people = {
        "Len": False,
        "Marquis": True,
        "Kylie": True,
        "Sandra": True
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