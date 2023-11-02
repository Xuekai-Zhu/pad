def solution():
    coin = True
    people = {
        "Quinton": False,
        "Sam": True,
        "Soledad": False,
        "Becca": True
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