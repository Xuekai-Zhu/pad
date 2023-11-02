def solution():
    coin = True
    people = {
        "Mickey": False,
        "Dom": True,
        "Lilly": True,
        "Eloy": False
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