def solution():
    coin = True
    people = {
        "Charles": False,
        "Emilio": False,
        "Vivek": True,
        "Steve": True
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