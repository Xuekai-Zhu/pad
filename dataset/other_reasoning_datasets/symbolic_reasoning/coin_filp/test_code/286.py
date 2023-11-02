def solution():
    coin = True
    people = {
        "Paris": False,
        "Jimmie": False,
        "Andrew": True,
        "Ramón": True
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