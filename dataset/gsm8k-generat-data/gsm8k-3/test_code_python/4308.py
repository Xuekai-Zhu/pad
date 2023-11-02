def solution():
    """John goes to the bakery to buy rolls. They sell them for 5 dollars for a dozen. He spent 15 dollars. How many rolls did he get?"""
    # Define the cost and quantity of rolls
    ROLL_COST_PER_DOZEN = 5
    ROLL_QUANTITY_PER_DOZEN = 12
    
    # Calculate the number of dozens of rolls John bought
    dozens_bought = 15 // ROLL_COST_PER_DOZEN
    
    # Calculate the total number of rolls John bought
    rolls_bought = dozens_bought * ROLL_QUANTITY_PER_DOZEN
    
    # Display the total number of rolls John bought
    result = rolls_bought
    return result

print(solution())