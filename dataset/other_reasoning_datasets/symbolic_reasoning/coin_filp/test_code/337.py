def solution():
    coin = True
    people = {
        "Delia": True,
        "Kathleen": False,
        "Mateo": True,
        "Marvin": False
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