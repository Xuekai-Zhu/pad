def solution():
    
    # Define the cost per scoop of ice cream
    COST_PER_SCOOP = 1.5

    # Define the number of scoops of ice cream Erin needs to buy
    num_scoops = 2

    # Define Erin's starting budget
    budget = 6.00

    # Calculate the number of scoops of ice cream Erin needs to buy
    num_scoops_needed = (budget - (num_scoops * COST_PER_SCOOP)) / COST_PER_SCOOP

    # Display the number of scoops of ice cream Erin needs to buy
    result = num_scoops_needed
    return result

print(solution())