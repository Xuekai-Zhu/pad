def solution():
    """Jenn is saving up money to buy a bike. She has 5 jars full of quarters. Each jar can hold 160 quarters. If the bike costs 180 dollars, how much money will she have left over after buying it?"""
    # Define the number of quarters in each jar and the value of a quarter
    QUARTERS_PER_JAR = 160
    QUARTER_VALUE = 0.25
    
    # Calculate the total value of the quarters
    total_quarters = 5 * QUARTERS_PER_JAR
    total_value = total_quarters * QUARTER_VALUE
    
    # Calculate how much money Jenn will have left over after buying the bike
    left_over = total_value - 180
    
    # Display the amount of money left over
    result = left_over
    return result

print(solution())