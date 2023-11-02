def solution():
    coin = True
    people = {
        "Kathy": False,
        "Elsa": True,
        "Alba": True,
        "Ivette": True
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