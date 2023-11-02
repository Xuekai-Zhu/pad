def solution():
    coin = True
    people = {
        "Stella": False,
        "Janis": True,
        "Darren": True,
        "Lena": False
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