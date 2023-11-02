def solution():
    coin = True
    people = {
        "Marco Antonio": True,
        "Suzette": False,
        "Roland": False,
        "Isabel": False
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