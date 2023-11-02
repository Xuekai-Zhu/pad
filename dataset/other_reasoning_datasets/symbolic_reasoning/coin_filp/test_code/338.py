def solution():
    coin = True
    people = {
        "Bj": True,
        "Rigo": False,
        "Nigel": True,
        "Christian": True
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