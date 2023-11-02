def solution():
    # Calculate the amount of money Samuel received
    samuel_share = 3/4 * 240

    # Calculate how much Samuel spent on drinks
    drinks_cost = 1/5 * 240

    # Calculate how much Samuel has left
    samuel_remaining = samuel_share - drinks_cost

    result = samuel_remaining
    return result

print(solution())