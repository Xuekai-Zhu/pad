def solution():
    coin = True
    people = {
        "Isaac": False,
        "Reyes": False,
        "Carly": True,
        "Tania": True
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