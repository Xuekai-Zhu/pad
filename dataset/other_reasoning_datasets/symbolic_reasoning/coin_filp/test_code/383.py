def solution():
    coin = True
    people = {
        "Geovanny": False,
        "Tom": True,
        "Katelyn": True,
        "Jennifer": True
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