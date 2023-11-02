def solution():
    coin = True
    people = {
        "Miguel Angel": True,
        "Saul": False,
        "Brady": False,
        "Darryl": True
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