def solution():
    coin = True
    people = {
        "Domingo": False,
        "Briana": True,
        "Michael": True,
        "Joan": False
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