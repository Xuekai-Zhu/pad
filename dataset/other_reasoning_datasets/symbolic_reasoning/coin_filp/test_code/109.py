def solution():
    coin = True
    people = {
        "Amy": True,
        "Ella": False,
        "Amilcar": False,
        "Roman": False
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