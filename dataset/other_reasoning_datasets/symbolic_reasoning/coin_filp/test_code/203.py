def solution():
    coin = True
    people = {
        "Dallas": False,
        "Uriel": True,
        "Brendan": True,
        "Julian": True
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