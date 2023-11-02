def solution():
    coin = True
    people = {
        "Ralph": False,
        "Jeanne": True,
        "Kyle": False,
        "Alejandro": False
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