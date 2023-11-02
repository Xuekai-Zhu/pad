def solution():
    coin = True
    people = {
        "Jacky": True,
        "Socorro": True,
        "Mark": True,
        "Wanda": False
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