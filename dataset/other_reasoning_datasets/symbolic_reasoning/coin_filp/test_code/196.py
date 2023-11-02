def solution():
    coin = True
    people = {
        "Salvador": False,
        "Sol": True,
        "Tyler": False,
        "Kareem": True
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