def solution():
    coin = True
    people = {
        "Letty": True,
        "Aimee": False,
        "Elvia": False,
        "Ted": False
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