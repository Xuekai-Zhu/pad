def solution():
    coin = True
    people = {
        "Skylar": True,
        "Chrissy": False,
        "Misty": True,
        "Kike": True
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