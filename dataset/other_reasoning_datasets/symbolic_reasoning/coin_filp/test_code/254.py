def solution():
    coin = True
    people = {
        "Guille": False,
        "Lisa": True,
        "Harvey": False,
        "Gina": False
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