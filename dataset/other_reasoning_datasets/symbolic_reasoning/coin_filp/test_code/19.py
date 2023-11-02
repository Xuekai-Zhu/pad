def solution():
    coin = True
    people = {
        "Penny": True,
        "Harry": False,
        "Jessica": False,
        "Horacio": True
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