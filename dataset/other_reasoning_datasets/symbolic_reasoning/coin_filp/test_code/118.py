def solution():
    coin = True
    people = {
        "Clarissa": False,
        "Shauna": False,
        "Alexis": False,
        "Branden": True
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