def solution():
    """Mrs. Lim milks her cows twice a day. Yesterday morning, she got 68 gallons of milk and in the evening, she got 82 gallons. This morning, she got 18 gallons fewer than she had yesterday morning. After selling some gallons of milk in the afternoon, Mrs. Lim has only 24 gallons left. How much was her revenue for the milk if each gallon costs $3.50?"""
    # Define the cost per gallon of milk
    COST_PER_GALLON = 3.50

    # Calculate the total amount of milk Mrs. Lim got yesterday
    yesterday_morning = 68
    yesterday_evening = 82
    yesterday_total = yesterday_morning + yesterday_evening

    # Calculate the amount of milk Mrs. Lim got this morning
    this_morning = yesterday_morning - 18

    # Calculate the total amount of milk Mrs. Lim had to sell
    total_milk = yesterday_total + this_morning

    # Calculate Mrs. Lim's revenue for the milk
    revenue = total_milk * COST_PER_GALLON

    # Display Mrs. Lim's revenue
    result = revenue
    return result

print(solution())