def solution():
    coin = True
    people = {
        "Britt": False,
        "Tamara": False,
        "Elvis": True,
        "Nayeli": False
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