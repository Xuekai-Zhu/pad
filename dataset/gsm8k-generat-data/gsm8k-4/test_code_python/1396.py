def solution():
    """Mrs. Lim milks her cows twice a day. Yesterday morning, she got 68 gallons of milk and in the evening, she got 82 gallons. This morning, she got 18 gallons fewer than she had yesterday morning. After selling some gallons of milk in the afternoon, Mrs. Lim has only 24 gallons left. How much was her revenue for the milk if each gallon costs $3.50?"""
    # Define the total gallons of milk produced
    total_milk = 68 + 82 + (68 - 18)

    # Calculate the gallons of milk sold
    sold_milk = total_milk - 24

    # Calculate the revenue from selling the milk
    revenue = sold_milk * 3.5
    
    result = revenue
    return result

print(solution())