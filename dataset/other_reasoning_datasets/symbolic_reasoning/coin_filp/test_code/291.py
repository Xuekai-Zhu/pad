def solution():
    coin = True
    people = {
        "Corey": True,
        "Elvin": False,
        "Tino": True,
        "Melvin": True
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