def solution():
    coin = True
    people = {
        "Sherri": False,
        "Genesis": True,
        "Jeffrey": False,
        "Samir": False
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