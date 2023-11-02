def solution():
    coin = True
    people = {
        "Latoya": True,
        "Eliseo": False,
        "Trina": True,
        "Melisa": False
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