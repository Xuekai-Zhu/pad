def solution():
    coin = True
    people = {
        "Guillermina": True,
        "Evelin": True,
        "Dominique": True,
        "Johnny": False
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