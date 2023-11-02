def solution():
    coin = True
    people = {
        "Renata": True,
        "Mariela": False,
        "Mona": False,
        "Kristin": True
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