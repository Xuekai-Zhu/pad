def solution():
    coin = True
    people = {
        "Fernanda": True,
        "Magda": True,
        "Elmer": True,
        "Alvaro": False
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