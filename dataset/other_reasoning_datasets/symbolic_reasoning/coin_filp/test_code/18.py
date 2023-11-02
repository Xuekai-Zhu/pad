def solution():
    coin = True
    people = {
        "Morgan": True,
        "Perla": False,
        "Joao": False,
        "Marta": False
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