def solution():
    coin = True
    people = {
        "Shawn": False,
        "Tracie": True,
        "Lynne": False,
        "Leila": True
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