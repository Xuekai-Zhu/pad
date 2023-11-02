def solution():
    """Four people in a law firm are planning a party. Mary will buy a platter of pasta for $20 and a loaf of bread for $2. Elle and Andrea will split the cost for buying 4 cans of soda which cost $1.50 each, and chicken wings for $10. Joe will buy a cake that costs $5. How much more will Mary spend than the rest of the firm put together?"""
    # Define the costs
    pasta_cost = 20
    bread_cost = 2
    soda_cost = 1.5
    wings_cost = 10
    cake_cost = 5

    # Calculate the total cost of Elle and Andrea's items
    soda_total_cost = 4 * soda_cost
    soda_per_person_cost = soda_total_cost / 2
    elle_andrea_total_cost = soda_per_person_cost + wings_cost

    # Calculate the total cost of all the items
    total_cost = pasta_cost + bread_cost + elle_andrea_total_cost + cake_cost

    # Calculate the cost Mary spent compared to the rest of the firm
    rest_of_firm_cost = elle_andrea_total_cost + cake_cost
    difference = total_cost - rest_of_firm_cost

    # Display the difference
    result = difference
    return result

print(solution())