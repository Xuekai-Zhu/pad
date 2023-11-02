def solution():
    coin = True
    people = {
        "Marcia": False,
        "Belen": False,
        "Reyna": True,
        "Britney": True
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