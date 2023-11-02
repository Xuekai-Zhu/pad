def solution():
    coin = True
    people = {
        "Ever": True,
        "Gio": True,
        "Elia": True,
        "Ramesh": False
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