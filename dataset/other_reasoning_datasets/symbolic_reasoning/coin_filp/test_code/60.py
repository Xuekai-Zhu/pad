def solution():
    coin = True
    people = {
        "Russ": True,
        "Berta": False,
        "Mandy": False,
        "Lydia": True
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