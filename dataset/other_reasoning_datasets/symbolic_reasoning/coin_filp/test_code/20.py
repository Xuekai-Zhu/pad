def solution():
    coin = True
    people = {
        "Axel": True,
        "Osvaldo": True,
        "Mildred": False,
        "Sylvia": True
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