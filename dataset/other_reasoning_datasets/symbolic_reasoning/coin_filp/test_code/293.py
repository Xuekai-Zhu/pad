def solution():
    coin = True
    people = {
        "Bri": False,
        "Roger": True,
        "Eve": False,
        "Diana": True
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