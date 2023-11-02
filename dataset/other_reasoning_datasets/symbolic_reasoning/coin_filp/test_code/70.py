def solution():
    coin = True
    people = {
        "Ron": True,
        "Carl": True,
        "Joann": False,
        "Young": True
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