def solution():
    coin = True
    people = {
        "Felipe": False,
        "Heidi": True,
        "Nino": False,
        "Bradley": False
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