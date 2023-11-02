def solution():
    coin = True
    people = {
        "King": True,
        "Edith": False,
        "Traci": True,
        "Flor": True
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