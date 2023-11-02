def solution():
    coin = True
    people = {
        "Dany": True,
        "Hilda": True,
        "Butch": True,
        "Mahesh": False
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