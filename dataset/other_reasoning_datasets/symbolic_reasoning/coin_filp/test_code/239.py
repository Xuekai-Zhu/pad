def solution():
    coin = True
    people = {
        "Miranda": False,
        "Jacques": False,
        "Clarence": True,
        "Chandra": True
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