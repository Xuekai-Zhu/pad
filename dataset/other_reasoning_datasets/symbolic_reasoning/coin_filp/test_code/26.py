def solution():
    coin = True
    people = {
        "Phillip": False,
        "Ajay": True,
        "Janie": True,
        "Augusto": True
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