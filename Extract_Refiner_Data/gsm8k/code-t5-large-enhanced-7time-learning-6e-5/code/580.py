def solution():
    
    # Define the number of contacts per box and the number of days
    num_contacts = 90
    num_days = 45

    # Calculate the total cost of the contacts before the discount
    total_cost_before_discount = num_contacts * 100 * num_days

    # Calculate the discount
    discount = total_cost_before_discount * 0.1

    # Calculate the total cost of the contacts after the discount
    total_cost_after_discount = total_cost_before_discount - discount

    # Calculate the cost per pair of contacts
    cost_per_pair = total_cost_after_discount / 2

    # Display the cost per pair of contacts
    result = cost_per_pair
    return result

print(solution())