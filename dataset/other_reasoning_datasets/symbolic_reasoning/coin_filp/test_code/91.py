def solution():
    coin = True
    people = {
        "Jesús": True,
        "Vidal": False,
        "Maxine": True,
        "Gloria": False
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