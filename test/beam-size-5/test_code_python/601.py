def solution():
    # Calculate the total amount earned from selling lemonade for 4 hours at $0.50 per cup
    earnings_4_hours = 15 * 0.5 * 4  # Patrick sold 15 cups of lemonade for 4 hours at $0.50 per cup

    # Calculate the total amount earned from selling lemonade for 2 hours at $0.60 per cup
    earnings_2_hours = 10 * 0.60 * 2  # Patrick sold 10 cups of lemonade for 2 hours at $0.60 per cup

    # Calculate the total amount earned from selling lemonade for 6 hours at $0.60 per cup
    total_earnings = earnings_4_hours + earnings_2_hours
    result = total_earnings
    return result

print(solution())