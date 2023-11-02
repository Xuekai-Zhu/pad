def solution():
    coin = True
    people = {
        "Williams": False,
        "Reza": True,
        "Ashton": True,
        "Lillian": True
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