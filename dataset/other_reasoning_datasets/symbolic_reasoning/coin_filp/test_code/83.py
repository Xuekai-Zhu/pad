def solution():
    coin = True
    people = {
        "Jorge Luis": False,
        "Mo": True,
        "Alexia": True,
        "Jerry": False
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