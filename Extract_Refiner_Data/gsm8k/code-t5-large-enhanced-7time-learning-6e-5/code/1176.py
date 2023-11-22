def solution():
    
    # Define the cost per gallon of milk
    COST_PER_GALLON = 3.5

    # Calculate the total amount of milk sold
    total_milk_sold = 4000 * COST_PER_GALLON

    # Calculate the amount of milk that could be sold with Mr. Marcellus
    sold_with_Marcellus = total_milk_sold * (2/5)

    # Calculate the refund amount
    refund_amount = sold_with_Marcellus * COST_PER_GALLON

    # Display the refund amount
    result = refund_amount
    return result

print(solution())