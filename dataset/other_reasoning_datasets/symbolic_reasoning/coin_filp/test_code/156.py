def solution():
    coin = True
    people = {
        "Reginald": False,
        "Franky": True,
        "Kira": True,
        "Gordon": True
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