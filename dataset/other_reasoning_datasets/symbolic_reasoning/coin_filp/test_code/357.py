def solution():
    coin = True
    people = {
        "Maria Elena": True,
        "Dewayne": False,
        "Mj": False,
        "Elliott": True
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