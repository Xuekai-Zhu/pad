def solution():
    """Frank has 7 one-dollar bills, 4 five-dollar bills, 2 ten-dollar bills, and 1 twenty-dollar bill. He goes to buy peanuts, which cost $3 a pound. He buys what he wants and has $4 in change. He plans to eat the peanuts all in one week. How many pounds does he eat on average per day?"""
    # Define the amount of money Frank has
    money = 7*1 + 4*5 + 2*10 + 1*20 - 4

    # Define the cost of the peanuts per pound
    peanut_price = 3

    # Calculate the maximum amount of peanuts Frank can buy
    max_peanut = money // peanut_price

    # Define the number of days Frank plans to eat the peanuts
    days = 7

    # Calculate the average amount of peanuts Frank eats per day
    average_peanut = max_peanut / days

    # Display the average amount of peanuts Frank eats per day
    result = average_peanut
    return result

print(solution())