def solution():
    coin = True
    people = {
        "Issa": True,
        "Kendra": True,
        "Ignacio": True,
        "Henry": True
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