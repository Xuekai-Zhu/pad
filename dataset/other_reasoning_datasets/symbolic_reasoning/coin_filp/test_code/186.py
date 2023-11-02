def solution():
    coin = True
    people = {
        "Héctor": True,
        "Daniela": True,
        "Rossy": True,
        "Jose Manuel": False
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