def solution():
    coin = True
    people = {
        "Gabby": False,
        "Reese": True,
        "Leah": False,
        "Celia": False
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