def solution():
    coin = True
    people = {
        "Jason": False,
        "Betty": True,
        "Elisa": True,
        "Jay": False
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