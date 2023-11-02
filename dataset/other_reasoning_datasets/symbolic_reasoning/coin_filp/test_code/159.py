def solution():
    coin = True
    people = {
        "Gabi": True,
        "Dante": True,
        "Rafa": True,
        "Tricia": False
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