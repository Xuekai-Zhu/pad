def solution():
    coin = True
    people = {
        "Brandon": False,
        "Ivonne": False,
        "Jefferson": True,
        "Isabella": False
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