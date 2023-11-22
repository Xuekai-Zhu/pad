def solution():
    
    # Define the cost of the first amusement park and the second amusement park
    AMOUNT_1_FEE = 26
    CHILD_1_FEE = 12
    AMOUNT_2_FEE = 14
    CHILD_2_FEE = 10

    # Define the number of adults and children in the family
    num_adults = 2
    num_children = 2

    # Calculate the total cost of the first amusement park
    total_cost_1 = AMOUNT_1_FEE * num_adults + CHILD_1_FEE * num_children

    # Calculate the total cost of the second amusement park
    total_cost_2 = AMOUNT_2_FEE * num_adults + CHILD_2_FEE * num_children

    # Calculate the amount saved by choosing the second amusement park over the first
    amount_saved = total_cost_1 - total_cost_2

    # Display the amount saved
    result

print(solution())