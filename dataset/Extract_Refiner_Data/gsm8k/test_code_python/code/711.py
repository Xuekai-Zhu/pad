def solution():
    
    # Define the initial planned cost of each computer
    initial_planned_cost = 700

    # Define the number of computers to be bought
    num_computers = 500

    # Calculate the new planned cost of each computer
    new_planned_cost = initial_planned_cost * 1.1

    # Calculate the new planned cost of all the computers
    new_planned_cost = new_planned_cost * num_computers

    # Calculate the total cost of buying the computers at the new prices
    total_cost = new_planned_cost * num_computers

    # return the result
    result = total_cost
    return result

print(solution())