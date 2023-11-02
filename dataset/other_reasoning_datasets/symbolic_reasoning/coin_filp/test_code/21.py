def solution():
    coin = True
    people = {
        "Emiliano": True,
        "Jasmin": True,
        "Wade": True,
        "Vilma": False
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