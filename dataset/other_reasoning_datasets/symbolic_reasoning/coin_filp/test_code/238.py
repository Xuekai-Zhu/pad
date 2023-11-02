def solution():
    coin = True
    people = {
        "Rahul": True,
        "Praveen": True,
        "Isaiah": True,
        "Elsie": False
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