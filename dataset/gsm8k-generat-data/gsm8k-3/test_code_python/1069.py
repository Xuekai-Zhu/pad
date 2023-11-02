def solution():
    """Maria has 4 dimes, 4 quarters, and 7 nickels in her piggy bank. Her mom gives her 5 quarters. How much money, in dollars, does Maria have now?"""
    # Define the value of each coin
    DIME_VALUE = 0.10
    QUARTER_VALUE = 0.25
    NICKEL_VALUE = 0.05
    
    # Calculate the total value Maria had before her mom gave her the quarters
    total_value = 4*DIME_VALUE + 4*QUARTER_VALUE + 7*NICKEL_VALUE
    
    # Add the value of the 5 quarters Maria's mom gives her
    total_value += 5*QUARTER_VALUE
    
    # Display the total value in dollars
    result = total_value
    return result

print(solution())