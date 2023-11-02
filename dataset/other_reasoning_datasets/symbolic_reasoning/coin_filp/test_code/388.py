def solution():
    coin = True
    people = {
        "Brooklyn": True,
        "Dawn": False,
        "Tay": True,
        "Gene": True
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