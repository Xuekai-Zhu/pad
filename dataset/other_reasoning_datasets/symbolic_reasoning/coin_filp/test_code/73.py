def solution():
    coin = True
    people = {
        "Gabe": False,
        "Dora": True,
        "Aileen": False,
        "Modesto": False
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