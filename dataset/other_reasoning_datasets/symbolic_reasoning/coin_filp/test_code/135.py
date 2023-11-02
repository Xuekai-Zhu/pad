def solution():
    coin = True
    people = {
        "Ronnie": True,
        "Kiki": True,
        "Alan": True,
        "Remy": True
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