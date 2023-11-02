def solution():
    # Calculate the total earned from selling red and blue stamps
    total_earned = (20 * 1.1) + (80 * 0.8)

    # Calculate the remaining earnings needed from selling yellow stamps
    remaining_earned = 100 - total_earned

    # Calculate the price needed to sell each yellow stamp at to earn the remaining amount
    yellow_stamps_needed = 7
    price_needed = remaining_earned / yellow_stamps_needed
    result = price_needed
    return result

print(solution())