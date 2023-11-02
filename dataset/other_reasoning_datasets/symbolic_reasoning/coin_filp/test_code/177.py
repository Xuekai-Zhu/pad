def solution():
    coin = True
    people = {
        "Ramona": False,
        "Lucy": True,
        "Gail": False,
        "Octavio": True
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