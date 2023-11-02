def solution():
    coin = True
    people = {
        "Ira": True,
        "Paola": True,
        "Jose Antonio": False,
        "Maria": False
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