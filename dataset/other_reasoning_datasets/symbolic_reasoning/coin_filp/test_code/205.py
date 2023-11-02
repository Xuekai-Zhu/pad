def solution():
    coin = True
    people = {
        "Frank": True,
        "Trevor": False,
        "Al": False,
        "Gabriella": True
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