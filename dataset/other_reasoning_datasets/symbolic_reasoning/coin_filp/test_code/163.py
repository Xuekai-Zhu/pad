def solution():
    coin = True
    people = {
        "Marcy": True,
        "Gonzalez": False,
        "Alice": False,
        "Arlene": True
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