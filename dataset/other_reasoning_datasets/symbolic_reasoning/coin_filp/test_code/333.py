def solution():
    coin = True
    people = {
        "Gee": False,
        "Joseluis": True,
        "Cory": False,
        "Stefanie": True
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