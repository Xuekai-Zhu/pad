def solution():
    coin = True
    people = {
        "Elle": True,
        "Alex": False,
        "Irma": True,
        "Stephan": True
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