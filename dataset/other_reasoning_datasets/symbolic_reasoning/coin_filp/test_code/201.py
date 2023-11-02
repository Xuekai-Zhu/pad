def solution():
    coin = True
    people = {
        "Belkis": False,
        "Wendell": True,
        "Lissette": False,
        "Patricia": False
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