def solution():
    coin = True
    people = {
        "Kristy": True,
        "Brandi": False,
        "Lizeth": False,
        "Petra": True
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