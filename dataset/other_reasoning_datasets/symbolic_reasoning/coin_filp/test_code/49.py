def solution():
    coin = True
    people = {
        "Rubi": False,
        "Daisy": False,
        "Yadira": True,
        "Santa": False
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