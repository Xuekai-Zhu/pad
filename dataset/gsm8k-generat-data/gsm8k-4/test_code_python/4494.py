def solution():
    """Thomas started saving for a car almost 2 years ago. For the first year, his weekly allowance was $50. In the second year, 
    he got a job that pays $9 an hour at a coffee shop and worked 30 hours a week, so his parents discontinued his allowance. 
    If the car he wants to buy is $15,000 and he spends $35 a week on himself, how much more money does Thomas need to buy 
    the car by the end of the 2 years?"""
    # Define the total amount of weeks
    TOTAL_WEEKS = 104

    # Calculate the total amount of money saved from Thomas' allowance in the first year
    year1_savings = 50 * 52

    # Calculate the total amount of money earned from Thomas' job in the second year
    year2_savings = 9 * 30 * 52

    # Subtract Thomas' personal expenses for 2 years
    personal_expenses = 35 * 104

    # Calculate the total savings over 2 years
    total_savings = year1_savings + year2_savings - personal_expenses

    # Calculate the amount of money Thomas still needs to buy the car
    remaining_money = 15000 - total_savings

    result = remaining_money
    return result

print(solution())