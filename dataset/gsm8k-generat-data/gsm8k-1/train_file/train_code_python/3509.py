def solution():
    """Alfred likes to save $1,000.00 over 12 months for his Christmas shopping. He has $100.00 left over from last year's holiday to put towards this year's goal. How much money does Alfred now need to save each month in order to reach his goal in 12 months?"""
    total_goal = 1000
    months_to_save = 12
    starting_amount = 100
    amount_left_to_save = total_goal - starting_amount
    amount_to_save_per_month = amount_left_to_save / months_to_save
    result = amount_to_save_per_month
    return result

print(solution())