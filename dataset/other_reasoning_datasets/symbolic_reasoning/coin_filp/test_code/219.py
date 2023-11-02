def solution():
    coin = True
    people = {
        "Selene": False,
        "Felix": False,
        "Milton": False,
        "Yessica": True
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