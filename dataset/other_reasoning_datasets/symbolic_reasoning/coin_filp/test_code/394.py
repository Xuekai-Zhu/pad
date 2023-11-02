def solution():
    coin = True
    people = {
        "Albert": False,
        "Felicia": False,
        "Margo": True,
        "Patty": False
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