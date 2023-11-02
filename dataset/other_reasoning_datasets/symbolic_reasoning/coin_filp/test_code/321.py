def solution():
    coin = True
    people = {
        "Maryam": False,
        "Susy": False,
        "Trinity": True,
        "Pearl": True
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