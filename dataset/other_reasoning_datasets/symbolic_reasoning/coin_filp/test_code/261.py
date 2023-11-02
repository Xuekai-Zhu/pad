def solution():
    coin = True
    people = {
        "Gabino": False,
        "Kayla": True,
        "Laurie": False,
        "Familia": True
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