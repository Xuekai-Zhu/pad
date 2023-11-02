def solution():
    # Calculate the total earnings from selling 8-inch portraits
    earnings_8_inch = 5 * 3  # she sells three 8-inch portraits per day

    # Calculate the total earnings from selling 16-inch portraits
    earnings_16_inch = 2 * (5 * 16)  # she sells five 16-inch portraits per day, at twice the price of the 8-inch portrait

    # Calculate the total earnings over 3 days
    total_earnings = 3 * (earnings_8_inch + earnings_16_inch)
    result = total_earnings
    return result

print(solution())