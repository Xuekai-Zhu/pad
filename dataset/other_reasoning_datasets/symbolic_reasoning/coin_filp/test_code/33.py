def solution():
    coin = True
    people = {
        "Ale": False,
        "Gaspar": True,
        "Sonny": False,
        "Simon": True
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