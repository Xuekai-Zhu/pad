def solution():
    coin = True
    people = {
        "Larissa": False,
        "Shawna": False,
        "Alma": True,
        "Paulette": False
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