def solution():
    coin = True
    people = {
        "Oscar": False,
        "George": False,
        "Sanjay": True,
        "Haydee": False
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