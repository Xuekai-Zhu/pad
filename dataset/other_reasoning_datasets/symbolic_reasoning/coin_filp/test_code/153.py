def solution():
    coin = True
    people = {
        "Bob": True,
        "Aman": False,
        "Richie": True,
        "Sana": False
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