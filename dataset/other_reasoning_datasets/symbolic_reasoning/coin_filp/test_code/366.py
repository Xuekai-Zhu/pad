def solution():
    coin = True
    people = {
        "Juliet": True,
        "Ricardo": False,
        "Tita": False,
        "Dianna": True
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