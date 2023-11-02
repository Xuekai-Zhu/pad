def solution():
    coin = True
    people = {
        "Shannon": False,
        "Millie": True,
        "Rosemary": False,
        "Priyanka": True
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