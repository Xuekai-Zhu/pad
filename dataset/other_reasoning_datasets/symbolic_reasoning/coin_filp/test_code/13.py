def solution():
    coin = True
    people = {
        "Jessy": False,
        "Libby": False,
        "Danielle": True,
        "Red": True
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