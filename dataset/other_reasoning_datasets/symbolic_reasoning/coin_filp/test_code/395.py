def solution():
    coin = True
    people = {
        "Noelia": True,
        "Cassidy": False,
        "Ashok": True,
        "Francisco": True
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