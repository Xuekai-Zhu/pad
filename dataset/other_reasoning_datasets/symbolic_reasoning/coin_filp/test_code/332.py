def solution():
    coin = True
    people = {
        "Lorraine": True,
        "Corinne": True,
        "Kate": True,
        "Floyd": True
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