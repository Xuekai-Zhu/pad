def solution():
    coin = True
    people = {
        "Dustin": True,
        "Luiz": False,
        "Rolando": True,
        "Connor": False
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