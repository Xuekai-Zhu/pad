def solution():
    
    # Define the cost of each cell phone and the number of cell phones purchased
    cell_phone_cost = 150
    num_cell_phones = 5

    # Calculate the total cost of the cell phones for 3 months
    total_cost = cell_phone_cost * num_cell_phones * 3

    # Calculate the interest charged for each unit
    interest_charged = total_cost * 0.02

    # Calculate the total cost for 3 months
    total_cost += interest_charged * num_cell_phones * 3

    # return the result
    result = total_cost
    return result

print(solution())