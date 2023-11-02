def solution():
    coin = True
    people = {
        "Kristine": False,
        "Van": True,
        "Marisol": True,
        "Preston": False
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