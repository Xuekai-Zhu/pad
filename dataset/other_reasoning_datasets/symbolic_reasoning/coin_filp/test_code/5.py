def solution():
    coin = True
    people = {
        "Jesse": True,
        "Roderick": True,
        "Travis": False,
        "Rita": False
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