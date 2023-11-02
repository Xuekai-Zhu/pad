def solution():
    coin = True
    people = {
        "Wally": True,
        "Claire": False,
        "Helen": True,
        "Nacho": False
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