def solution():
    coin = True
    people = {
        "Billy": True,
        "Kassandra": True,
        "Joy": False,
        "Abe": True
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