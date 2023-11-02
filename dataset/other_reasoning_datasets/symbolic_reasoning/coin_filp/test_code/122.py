def solution():
    coin = True
    people = {
        "Scotty": True,
        "Edgar": True,
        "Hanna": True,
        "Austin": True
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