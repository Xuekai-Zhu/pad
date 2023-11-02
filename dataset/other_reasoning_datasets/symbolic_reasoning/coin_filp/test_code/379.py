def solution():
    coin = True
    people = {
        "Jermaine": True,
        "Pat": False,
        "Tammie": True,
        "Olivia": True
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