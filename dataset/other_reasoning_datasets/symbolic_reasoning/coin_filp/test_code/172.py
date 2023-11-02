def solution():
    coin = True
    people = {
        "Deon": True,
        "Lane": True,
        "Everett": True,
        "Lindsay": True
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