def solution():
    coin = True
    people = {
        "Sunil": True,
        "Tiana": False,
        "Darla": False,
        "Darnell": True
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