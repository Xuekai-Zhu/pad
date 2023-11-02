def solution():
    coin = True
    people = {
        "Ari": True,
        "Jasmine": False,
        "Elliot": True,
        "Kendrick": True
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