def solution():
    coin = True
    people = {
        "Tomas": False,
        "Nic": True,
        "Zoila": True,
        "Calvin": False
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