def solution():
    coin = True
    people = {
        "Edwin": True,
        "Lovely": False,
        "Curt": True,
        "Damon": True
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