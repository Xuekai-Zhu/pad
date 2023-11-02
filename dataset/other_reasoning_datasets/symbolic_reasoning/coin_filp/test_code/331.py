def solution():
    coin = True
    people = {
        "Blanca": False,
        "Monika": False,
        "Ervin": False,
        "Lori": True
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