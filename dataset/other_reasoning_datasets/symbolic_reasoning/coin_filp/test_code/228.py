def solution():
    coin = True
    people = {
        "Idalia": True,
        "Arnoldo": False,
        "Marla": False,
        "Duane": False
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