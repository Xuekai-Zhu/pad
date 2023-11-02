def solution():
    coin = True
    people = {
        "Imelda": True,
        "Andi": True,
        "Mack": False,
        "Rigoberto": True
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