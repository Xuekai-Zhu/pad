def solution():
    coin = True
    people = {
        "Blake": True,
        "Hunter": True,
        "Lou": True,
        "Spencer": False
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