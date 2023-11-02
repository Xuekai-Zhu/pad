def solution():
    coin = True
    people = {
        "Fred": True,
        "Nolan": True,
        "Johnathan": True,
        "Carson": False
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