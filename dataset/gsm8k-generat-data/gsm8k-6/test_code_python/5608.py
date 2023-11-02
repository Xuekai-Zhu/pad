def solution():
    # Calculate the total revenue from selling watermelons
    revenue = 105 + (18 * 3)  # $105 profit plus revenue from selling 18 watermelons at $3 each

    # Calculate the cost of the watermelons
    cost = 18 * x  # Let x be the cost of each watermelon

    # Calculate the number of watermelons Carl started out with
    start = (revenue - cost) / x

    result = start
    return result

print(solution())