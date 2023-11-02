def solution():
    coin = True
    people = {
        "Sonya": True,
        "Eddy": False,
        "Carol": False,
        "Yung": True
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