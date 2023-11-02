def solution():
    coin = True
    people = {
        "Jose Luis": False,
        "Kiara": True,
        "Arun": False,
        "Josefina": False
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