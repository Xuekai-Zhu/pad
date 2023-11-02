def solution():
    coin = True
    people = {
        "Ivy": True,
        "Romeo": False,
        "Jana": True,
        "Ej": False
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