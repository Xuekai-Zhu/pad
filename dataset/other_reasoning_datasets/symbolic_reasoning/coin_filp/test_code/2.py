def solution():
    coin = True
    people = {
        "Angelina": True,
        "Layla": True,
        "Jenny": True,
        "Zane": False
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