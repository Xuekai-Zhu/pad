def solution():
    coin = True
    people = {
        "June": True,
        "Robin": False,
        "Josie": True,
        "Bo": False
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