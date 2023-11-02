def solution():
    """Jenn is saving up money to buy a bike. She has 5 jars full of quarters. Each jar can hold 160 quarters. If the bike costs 180 dollars, how much money will she have left over after buying it?"""
    # Define the cost of the bike and the value of each quarter
    bike_cost = 180
    quarter_value = 0.25

    # Calculate the total value of the quarters
    total_quarters = 5 * 160
    total_value = total_quarters * quarter_value

    # Calculate how much money Jenn will have left over after buying the bike
    leftover_money = total_value - bike_cost

    # Return the result
    result = leftover_money
    return result

print(solution())