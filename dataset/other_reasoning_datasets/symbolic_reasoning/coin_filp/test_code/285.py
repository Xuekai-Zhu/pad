def solution():
    coin = True
    people = {
        "Pedro": True,
        "Leopoldo": False,
        "Tee": False,
        "Mar": True
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