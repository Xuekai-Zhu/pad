def solution():
    coin = True
    people = {
        "Natalie": True,
        "Gilbert": True,
        "Brian": False,
        "Sanchez": False
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