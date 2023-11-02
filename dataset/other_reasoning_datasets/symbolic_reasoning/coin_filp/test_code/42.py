def solution():
    coin = True
    people = {
        "Shari": True,
        "Bella": True,
        "Liza": False,
        "Maira": False
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