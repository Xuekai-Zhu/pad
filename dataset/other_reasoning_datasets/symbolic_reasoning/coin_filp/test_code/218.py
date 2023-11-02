def solution():
    coin = True
    people = {
        "Teri": False,
        "Lina": False,
        "Mery": True,
        "Melanie": True
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