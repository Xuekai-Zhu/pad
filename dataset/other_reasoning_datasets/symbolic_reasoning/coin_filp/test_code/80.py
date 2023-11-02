def solution():
    coin = True
    people = {
        "April": False,
        "Molly": False,
        "Maurice": True,
        "Jaclyn": True
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