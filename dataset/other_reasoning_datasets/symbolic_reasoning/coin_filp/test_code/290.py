def solution():
    coin = True
    people = {
        "Dan": False,
        "Ruth": False,
        "Xavier": True,
        "Isidro": False
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