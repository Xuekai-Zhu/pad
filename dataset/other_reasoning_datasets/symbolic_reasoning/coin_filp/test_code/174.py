def solution():
    coin = True
    people = {
        "Lesley": True,
        "Luna": True,
        "Nadia": False,
        "Adriana": True
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