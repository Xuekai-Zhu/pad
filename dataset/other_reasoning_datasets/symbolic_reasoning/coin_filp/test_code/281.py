def solution():
    coin = True
    people = {
        "Carlitos": True,
        "Damaris": True,
        "Nikhil": False,
        "Jennie": False
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