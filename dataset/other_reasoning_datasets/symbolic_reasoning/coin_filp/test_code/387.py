def solution():
    coin = True
    people = {
        "Pauline": False,
        "Kerry": False,
        "Jeannette": True,
        "Hope": True
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