def solution():
    coin = True
    people = {
        "Ericka": False,
        "Aly": True,
        "Darius": False,
        "Reed": True
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