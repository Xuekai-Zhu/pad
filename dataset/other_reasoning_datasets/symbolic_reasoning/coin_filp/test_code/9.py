def solution():
    coin = True
    people = {
        "Jae": False,
        "Dennis": False,
        "Cris": True,
        "Bernadette": True
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