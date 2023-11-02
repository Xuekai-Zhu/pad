def solution():
    coin = True
    people = {
        "Margaret": False,
        "Rosi": True,
        "Willy": True,
        "Charlene": False
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