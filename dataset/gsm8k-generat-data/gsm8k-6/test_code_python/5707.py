def solution():
    # Calculate the total earnings from selling red and blue stamps
    earnings_red = 20 * 1.1  # sold 20 red stamps for $1.1 each
    earnings_blue = 80 * 0.8  # sold 80 blue stamps for $0.8 each
    total_earnings = earnings_red + earnings_blue

    # Calculate the amount needed to earn from selling yellow stamps
    remaining_earnings = 100 - total_earnings
    yellow_stamps_needed = 7
    price_per_yellow_stamp = round(remaining_earnings / yellow_stamps_needed, 2)
    result = price_per_yellow_stamp
    return result

print(solution())