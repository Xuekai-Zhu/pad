def solution():
    coin = True
    people = {
        "Janet": False,
        "Ant": False,
        "Vickie": True,
        "Elias": True
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