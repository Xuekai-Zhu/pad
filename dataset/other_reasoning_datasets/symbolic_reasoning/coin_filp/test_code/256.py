def solution():
    coin = True
    people = {
        "Johan": True,
        "Damien": True,
        "Serena": True,
        "Grace": True
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