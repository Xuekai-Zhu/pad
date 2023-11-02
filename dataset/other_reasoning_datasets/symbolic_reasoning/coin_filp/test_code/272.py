def solution():
    coin = True
    people = {
        "Flora": True,
        "Warren": True,
        "Gwendolyn": False,
        "Alissa": False
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