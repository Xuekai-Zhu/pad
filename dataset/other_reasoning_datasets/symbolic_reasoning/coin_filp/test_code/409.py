def solution():
    coin = True
    people = {
        "Emanuel": False,
        "Cheyenne": False,
        "Perez": True,
        "Yvette": False
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