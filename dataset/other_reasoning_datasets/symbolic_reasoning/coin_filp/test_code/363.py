def solution():
    coin = True
    people = {
        "Alain": True,
        "Jerome": False,
        "Kristina": False,
        "Ida": False
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