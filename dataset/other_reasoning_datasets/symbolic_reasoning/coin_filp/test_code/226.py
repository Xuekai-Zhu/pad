def solution():
    coin = True
    people = {
        "Damian": True,
        "Crystal": True,
        "Nisha": True,
        "Hernan": False
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