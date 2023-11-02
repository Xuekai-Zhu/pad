def solution():
    """Chad saves 40% of the money he earns/receives in a year.  This year, he made $600 mowing yards and received $250.00 for his birthday/holidays.  He also made $150.00 by selling some old video games and another $150.00 doing odd jobs.  How much will he save?"""
    # Define the amount of money Chad made in each category
    mowing_money = 600
    holiday_money = 250
    game_money = 150
    odd_job_money = 150

    # Calculate the total amount of money Chad made
    total_money = mowing_money + holiday_money + game_money + odd_job_money

    # Calculate the amount Chad will save
    saving_amount = total_money * 0.4

    # Display the saving amount
    result = saving_amount
    return result

print(solution())