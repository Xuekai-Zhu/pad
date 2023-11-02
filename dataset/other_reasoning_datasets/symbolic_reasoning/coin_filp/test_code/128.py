def solution():
    coin = True
    people = {
        "Kyra": False,
        "Luciano": True,
        "Ciara": False,
        "Bryan": True
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