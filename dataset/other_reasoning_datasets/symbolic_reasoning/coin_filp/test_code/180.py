def solution():
    coin = True
    people = {
        "Efren": True,
        "Rex": True,
        "Marilyn": True,
        "Emerson": True
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