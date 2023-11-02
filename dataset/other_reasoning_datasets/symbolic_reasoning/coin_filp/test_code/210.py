def solution():
    coin = True
    people = {
        "Noah": False,
        "Aubrey": True,
        "Cesar": False,
        "Eliana": False
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