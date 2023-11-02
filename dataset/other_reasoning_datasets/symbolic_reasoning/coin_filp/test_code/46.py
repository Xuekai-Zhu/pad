def solution():
    coin = True
    people = {
        "Marian": False,
        "Joanne": True,
        "Darrin": False,
        "Rohit": False
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