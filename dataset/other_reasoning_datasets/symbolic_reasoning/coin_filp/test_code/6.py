def solution():
    coin = True
    people = {
        "Cinthia": False,
        "Lloyd": False,
        "Jacqueline": True,
        "Jc": True
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