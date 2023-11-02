def solution():
    coin = True
    people = {
        "Tiara": True,
        "Araceli": True,
        "Michaela": True,
        "Genaro": False
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