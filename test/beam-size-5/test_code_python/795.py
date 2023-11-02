def solution():
    
    # Define the cost of a loaf of bread and a bagel of bread
    LOAF_COST = 2
    BAGEL_COST = 1

    # Define the number of loaves of bread and bagels of bread
    num_loaves = 3
    num_bagels = 2

    # Calculate the total cost of 3 loaves of bread
    total_cost_3_loaves = num_loaves * LOAF_COST

    # Calculate the total cost of 2 bagels of bread
    total_cost_2_bagels = num_bagels * BAGEL_COST

    # Calculate the difference in cost between 3 loaves of bread and 2 bagels
    cost_difference = total_cost_3_loaves - total_cost_2_bagels

    # Display the difference in cost
    result = cost_difference
    return result

print(solution())