def solution():
    coin = True
    people = {
        "Vijay": True,
        "Sherrie": False,
        "Doug": False,
        "Suzy": True
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