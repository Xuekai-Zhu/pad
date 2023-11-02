def solution():
    coin = True
    people = {
        "Cruz": False,
        "Wilber": True,
        "Marilu": True,
        "Malik": True
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