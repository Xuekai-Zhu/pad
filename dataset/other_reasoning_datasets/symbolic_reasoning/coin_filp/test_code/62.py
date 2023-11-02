def solution():
    coin = True
    people = {
        "Carole": True,
        "William": True,
        "Tiffany": True,
        "Hilary": False
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