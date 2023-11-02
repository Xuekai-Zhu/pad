def solution():
    coin = True
    people = {
        "Juan Manuel": True,
        "Benjamin": True,
        "Rory": False,
        "Rafael": True
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