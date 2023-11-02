def solution():
    coin = True
    people = {
        "Deanna": False,
        "Terri": False,
        "Gabriela": True,
        "Jonah": True
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