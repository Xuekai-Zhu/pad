def solution():
    coin = True
    people = {
        "Noelle": False,
        "Byron": True,
        "Jane": False,
        "Darin": False
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