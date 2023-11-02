def solution():
    coin = True
    people = {
        "Marcos": False,
        "Kerri": True,
        "Fabio": True,
        "Stephen": True
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