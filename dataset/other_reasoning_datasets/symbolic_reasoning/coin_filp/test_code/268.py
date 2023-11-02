def solution():
    coin = True
    people = {
        "Darwin": True,
        "Colin": True,
        "Cj": True,
        "Abhishek": True
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