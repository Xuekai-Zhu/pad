def solution():
    coin = True
    people = {
        "Alec": True,
        "Arianna": True,
        "Corina": True,
        "Juancarlos": True
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