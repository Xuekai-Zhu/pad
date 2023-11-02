def solution():
    coin = True
    people = {
        "Janette": False,
        "Stacey": True,
        "Ronny": True,
        "Kim": False
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