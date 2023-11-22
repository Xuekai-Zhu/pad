def solution():
    
    # Define the cost of a loaf and a bagel
    LOA_COST = 2
    BAGEL_COST = 1

    # Define the number of loaves and bagels
    NUM_LOAVES = 3
    NUM_BAGELS = 2

    # Calculate the total cost of 3 loaves of bread
    loaf_cost_total = LOA_COST * NUM_LOAVES

    # Calculate the total cost of 2 bagels of bread
    bagel_cost_total = BAGEL_COST * NUM_BAGELS

    # Calculate the difference in cost between 3 loaves and 2 bagels
    cost_difference = loaf_cost_total - bagel_cost_total

    # Display the cost difference
    result = cost_difference
    return result

print(solution())