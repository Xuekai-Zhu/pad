def solution():
    coin = True
    people = {
        "Lucio": True,
        "Víctor": False,
        "Lester": True,
        "Allie": True
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