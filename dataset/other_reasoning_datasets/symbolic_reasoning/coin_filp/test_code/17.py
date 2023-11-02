def solution():
    coin = True
    people = {
        "Kristopher": False,
        "Deb": True,
        "Jake": True,
        "Tammy": True
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