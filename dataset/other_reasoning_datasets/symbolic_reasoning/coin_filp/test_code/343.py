def solution():
    coin = True
    people = {
        "Leon": False,
        "Payton": True,
        "Stefan": True,
        "Javi": True
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