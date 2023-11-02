def solution():
    coin = True
    people = {
        "Bernard": False,
        "Lidia": True,
        "Sebastian": False,
        "Judy": False
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