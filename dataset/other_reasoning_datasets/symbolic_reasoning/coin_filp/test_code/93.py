def solution():
    coin = True
    people = {
        "Anastasia": False,
        "Thelma": True,
        "Sheri": True,
        "Rosita": True
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