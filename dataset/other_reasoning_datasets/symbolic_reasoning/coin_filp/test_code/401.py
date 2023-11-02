def solution():
    coin = True
    people = {
        "Hailey": True,
        "Avi": True,
        "Bree": False,
        "Samira": True
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