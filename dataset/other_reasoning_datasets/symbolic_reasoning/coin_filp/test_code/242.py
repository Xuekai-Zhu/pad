def solution():
    coin = True
    people = {
        "Clark": False,
        "Jenn": True,
        "Diane": True,
        "Blair": False
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