def solution():
    coin = True
    people = {
        "Marshall": True,
        "Herman": False,
        "Faye": False,
        "Grant": False
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