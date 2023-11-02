def solution():
    coin = True
    people = {
        "Carissa": True,
        "Paige": False,
        "Consuelo": False,
        "Izzy": True
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