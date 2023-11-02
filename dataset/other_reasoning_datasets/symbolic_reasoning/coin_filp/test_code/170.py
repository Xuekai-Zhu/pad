def solution():
    coin = True
    people = {
        "Lionel": True,
        "Fiona": True,
        "Bobby": False,
        "Janeth": False
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