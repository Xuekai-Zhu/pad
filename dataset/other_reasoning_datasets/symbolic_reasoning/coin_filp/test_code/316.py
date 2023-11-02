def solution():
    coin = True
    people = {
        "Bill": True,
        "Santos": False,
        "Roxy": True,
        "Randi": True
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