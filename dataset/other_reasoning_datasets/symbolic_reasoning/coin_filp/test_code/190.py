def solution():
    coin = True
    people = {
        "Yamileth": True,
        "Dane": True,
        "Aron": True,
        "Dee": False
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