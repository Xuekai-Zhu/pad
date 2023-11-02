def solution():
    coin = True
    people = {
        "Elva": True,
        "Kari": True,
        "Shirley": False,
        "Gilberto": True
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