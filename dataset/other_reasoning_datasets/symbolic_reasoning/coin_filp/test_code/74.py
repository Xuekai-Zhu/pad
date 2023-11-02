def solution():
    coin = True
    people = {
        "Victoria": True,
        "Aurora": False,
        "Amalia": False,
        "Princess": False
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