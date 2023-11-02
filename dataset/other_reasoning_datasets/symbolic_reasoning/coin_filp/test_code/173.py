def solution():
    coin = True
    people = {
        "Ubaldo": False,
        "Katrina": True,
        "Francis": False,
        "Lynn": True
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