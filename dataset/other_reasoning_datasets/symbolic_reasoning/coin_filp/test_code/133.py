def solution():
    coin = True
    people = {
        "Talia": True,
        "Nicki": False,
        "Tia": True,
        "Divya": False
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