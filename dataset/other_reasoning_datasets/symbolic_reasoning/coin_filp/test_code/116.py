def solution():
    coin = True
    people = {
        "Cristian": True,
        "Nik": False,
        "Gwen": True,
        "Josiah": True
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