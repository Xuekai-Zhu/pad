def solution():
    coin = True
    people = {
        "Teresa": True,
        "Reid": False,
        "Karin": False,
        "Gracie": False
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