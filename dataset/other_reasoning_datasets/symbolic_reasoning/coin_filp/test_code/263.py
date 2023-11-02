def solution():
    coin = True
    people = {
        "Conrad": True,
        "Marcella": False,
        "Annette": True,
        "Esteban": True
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