def solution():
    coin = True
    people = {
        "Russell": False,
        "Mitchell": False,
        "Bee": True,
        "Faith": False
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