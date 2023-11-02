def solution():
    coin = True
    people = {
        "Anil": False,
        "Enrique": True,
        "Jimmy": True,
        "Jhonny": False
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