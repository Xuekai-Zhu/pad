def solution():
    coin = True
    people = {
        "Timmy": False,
        "Katherine": False,
        "Gabriel": True,
        "Nate": False
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