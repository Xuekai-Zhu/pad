def solution():
    coin = True
    people = {
        "Christina": False,
        "Edna": True,
        "Ileana": True,
        "Lynette": True
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