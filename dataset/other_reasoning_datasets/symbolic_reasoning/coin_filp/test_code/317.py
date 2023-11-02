def solution():
    coin = True
    people = {
        "Lara": False,
        "Greg": False,
        "Ethan": True,
        "Terrence": True
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