def solution():
    coin = True
    people = {
        "Debora": False,
        "Jayson": False,
        "Donna": True,
        "Sai": False
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