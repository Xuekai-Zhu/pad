def solution():
    coin = True
    people = {
        "Missy": True,
        "Erin": True,
        "Lorna": True,
        "Lenny": True
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