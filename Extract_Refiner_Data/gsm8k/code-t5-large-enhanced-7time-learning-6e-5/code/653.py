def solution():
    
    # Define the cost of the plane and the expenses for renting and maintaining
    plane_cost = 150000
    rent_expenses = 5000
    fuel_expenses = rent_expenses * 2

    # Calculate the total expenses for the first year
    total_expenses = rent_expenses + fuel_expenses

    # Calculate the total cost for the first year
    total_cost_year = plane_cost + total_expenses + total_expenses

    # Display the total cost for the first year
    result = total_cost_year
    return result

print(solution())