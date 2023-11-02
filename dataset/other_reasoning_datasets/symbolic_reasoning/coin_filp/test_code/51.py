def solution():
    coin = True
    people = {
        "Manish": False,
        "Lu": True,
        "Karl": False,
        "Don": True
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