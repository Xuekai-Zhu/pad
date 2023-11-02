def solution():
    coin = True
    people = {
        "Jody": False,
        "Juan": False,
        "Rebekah": True,
        "Kaylee": True
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