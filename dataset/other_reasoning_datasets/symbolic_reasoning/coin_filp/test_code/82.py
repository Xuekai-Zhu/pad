def solution():
    coin = True
    people = {
        "Matilde": False,
        "Jan": True,
        "Marcel": False,
        "Mimi": False
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