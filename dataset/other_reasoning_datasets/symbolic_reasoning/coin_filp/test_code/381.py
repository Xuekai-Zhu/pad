def solution():
    coin = True
    people = {
        "Theo": True,
        "Sheila": True,
        "Mariana": False,
        "Esmeralda": True
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