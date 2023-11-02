def solution():
    """Leila bought a living room set consisting of a sofa worth $1,250, 2 armchairs costing $425 each and a coffee table. The total amount of the invoice is $2,430. What is the price of the coffee table?"""
    # Define the costs of the sofa and armchairs
    sofa_cost = 1250
    armchair_cost = 425

    # Define the total amount of the invoice
    total_cost = 2430

    # Calculate the total cost of the sofas and armchairs
    sofas_and_armchairs_cost = sofa_cost + (2 * armchair_cost)

    # Calculate the cost of the coffee table
    coffee_table_cost = total_cost - sofas_and_armchairs_cost

    # Display the cost of the coffee table
    result = coffee_table_cost
    return result

print(solution())