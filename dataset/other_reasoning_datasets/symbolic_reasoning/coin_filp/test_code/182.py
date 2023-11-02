def solution():
    coin = True
    people = {
        "Kendall": False,
        "Matias": True,
        "Kaleb": True,
        "Randy": False
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