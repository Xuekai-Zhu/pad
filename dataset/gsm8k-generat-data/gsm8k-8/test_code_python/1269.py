def solution():
    # Define the cost of each service
    federal_cost = 50
    state_cost = 30
    quarterly_cost = 80

    # Define the number of services sold
    federal_sold = 60
    state_sold = 20
    quarterly_sold = 10

    # Calculate the total revenue for the day
    total_revenue = (federal_cost * federal_sold) + (state_cost * state_sold) + (quarterly_cost * quarterly_sold)
    result = total_revenue
    return result

print(solution())