def solution():
    coin = True
    people = {
        "Aj": False,
        "Jd": True,
        "Maddie": False,
        "Francisca": False
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