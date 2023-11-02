def solution():
    coin = True
    people = {
        "Mya": True,
        "Fernando": True,
        "Bubba": False,
        "Tommy": False
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