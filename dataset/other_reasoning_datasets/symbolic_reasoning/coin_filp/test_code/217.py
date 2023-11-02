def solution():
    coin = True
    people = {
        "Kristie": False,
        "Johnnie": True,
        "Marisa": True,
        "Derick": False
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