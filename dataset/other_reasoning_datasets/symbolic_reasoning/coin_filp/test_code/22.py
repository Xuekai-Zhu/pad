def solution():
    coin = True
    people = {
        "Lino": False,
        "Mariel": False,
        "Aditya": False,
        "Elisabeth": True
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