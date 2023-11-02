def solution():
    coin = True
    people = {
        "Karen": False,
        "Hector": True,
        "Mai": True,
        "Steven": True
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