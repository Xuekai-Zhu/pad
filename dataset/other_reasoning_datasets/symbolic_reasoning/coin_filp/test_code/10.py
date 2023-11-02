def solution():
    coin = True
    people = {
        "Hank": False,
        "Janine": False,
        "Frankie": True,
        "Isa": True
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