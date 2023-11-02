def solution():
    coin = True
    people = {
        "Oswaldo": False,
        "José Luis": True,
        "Sheldon": False,
        "Tara": True
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