def solution():
    coin = True
    people = {
        "Tim": True,
        "Candace": True,
        "Cecil": False,
        "Misael": True
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