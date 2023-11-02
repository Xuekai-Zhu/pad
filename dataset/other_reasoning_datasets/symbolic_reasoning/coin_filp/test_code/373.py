def solution():
    coin = True
    people = {
        "Stevie": False,
        "Julie": True,
        "Leonard": False,
        "Karina": True
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