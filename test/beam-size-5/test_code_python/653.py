def solution():
    
    # Define the cost of the plane and the monthly rent and fuel
    plane_cost = 150000
    monthly_rental_cost = 5000
    fuel_cost_per_month = monthly_rental_cost * 2

    # Calculate the total monthly expenses
    monthly_expenses = monthly_rental_cost + fuel_cost_per_month

    # Calculate the total yearly expenses
    yearly_expenses = monthly_rental_cost * 12

    # Calculate the total cost for the first year
    total_cost = yearly_expenses + yearly_expenses

    # Display the total cost
    result = total_cost
    return result

print(solution())