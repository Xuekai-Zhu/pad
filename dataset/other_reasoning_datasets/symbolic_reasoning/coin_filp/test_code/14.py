def solution():
    coin = True
    people = {
        "Jorge": False,
        "Natalia": False,
        "Bryant": True,
        "Kiran": True
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