def solution():
    coin = True
    people = {
        "Wilson": False,
        "Abbey": False,
        "Harold": True,
        "Nelly": True
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