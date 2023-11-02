def solution():
    coin = True
    people = {
        "Ruben": True,
        "Bernardo": True,
        "Ariel": False,
        "Shelley": True
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