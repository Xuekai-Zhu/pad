def solution():
    coin = True
    people = {
        "Donovan": False,
        "Lonnie": False,
        "Jairo": True,
        "Mariah": True
    }
    for person, flips in people.items():
        if flips:
            # Flip the coin by reversing its current state
            coin = not coin
    if coin:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())