def solution():
    """For 6 weeks in the summer, Erica treats herself to 1 ice cream cone from the ice cream truck. Monday, Wednesday and Friday she gets a $2.00 orange creamsicle. Tuesday and Thursday she gets a $1.50 ice cream sandwich. Saturday and Sunday she gets a $3.00 Nutty-Buddy. How much money does she spend on ice cream in 6 weeks?"""
    # Define the prices of each ice cream cone
    creamsicle_price = 2.00
    sandwich_price = 1.50
    nuttybuddy_price = 3.00

    # Calculate the total cost of ice cream for 6 weeks
    total_cost = (3 * creamsicle_price + 2 * sandwich_price + 2 * nuttybuddy_price) * 6

    result = total_cost
    return result

print(solution())