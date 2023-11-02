def solution():
    """Frank has 7 one-dollar bills, 4 five-dollar bills, 2 ten-dollar bills, and 1 twenty-dollar bill. He goes to buy peanuts, which cost $3 a pound. He buys what he wants and has $4 in change. He plans to eat the peanuts all in one week. How many pounds does he eat on average per day?"""
    # Define the amount of money Frank has
    money = 7 + 4*5 + 2*10 + 20 - 4

    # Define the cost of peanuts per pound and calculate the maximum number of pounds Frank can buy
    cost_per_pound = 3
    max_pounds = money // cost_per_pound

    # Calculate the average number of pounds Frank eats per day
    days = 7
    pounds_per_day = max_pounds / days

    # Return the result
    result = pounds_per_day
    return result

print(solution())