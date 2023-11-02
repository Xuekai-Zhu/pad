def solution():
    coin = True
    people = {
        "Celso": False,
        "Tracy": False,
        "Winston": True,
        "Anton": False
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