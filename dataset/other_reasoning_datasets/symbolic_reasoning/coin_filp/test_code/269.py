def solution():
    coin = True
    people = {
        "Lupita": True,
        "Cyndi": True,
        "Kay": False,
        "Derrick": True
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