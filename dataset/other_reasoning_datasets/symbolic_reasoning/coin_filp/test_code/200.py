def solution():
    coin = True
    people = {
        "Emma": True,
        "Maryann": True,
        "Olga": False,
        "Nataly": True
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