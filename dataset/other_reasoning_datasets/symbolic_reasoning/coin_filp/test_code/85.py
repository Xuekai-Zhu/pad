def solution():
    coin = True
    people = {
        "Nabil": False,
        "Marlene": False,
        "Wendy": True,
        "Jillian": False
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