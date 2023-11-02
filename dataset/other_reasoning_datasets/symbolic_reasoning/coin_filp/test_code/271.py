def solution():
    coin = True
    people = {
        "Dorian": True,
        "Mayra": True,
        "Freddie": False,
        "Magaly": True
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