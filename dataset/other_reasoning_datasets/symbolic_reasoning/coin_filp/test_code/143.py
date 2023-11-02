def solution():
    coin = True
    people = {
        "Tucker": False,
        "Daniel": True,
        "Hernandez": False,
        "Alison": True
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