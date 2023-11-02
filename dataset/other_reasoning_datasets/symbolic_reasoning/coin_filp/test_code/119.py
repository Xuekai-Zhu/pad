def solution():
    coin = True
    people = {
        "Barb": False,
        "Gage": True,
        "Kristian": True,
        "Asia": False
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