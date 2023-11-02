def solution():
    coin = True
    people = {
        "Andre": False,
        "Oralia": False,
        "Carrie": True,
        "Bruno": False
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