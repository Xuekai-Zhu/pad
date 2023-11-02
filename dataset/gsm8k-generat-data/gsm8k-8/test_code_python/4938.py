def solution():
    # Define the total number of cartons and the number of customers
    total_cartons = 400
    num_customers = 4

    # Calculate the number of cartons delivered to each customer
    cartons_per_customer = total_cartons / num_customers

    # Subtract the number of damaged cartons from each customer's delivery
    accepted_cartons_per_customer = cartons_per_customer - 60

    # Calculate the total number of accepted cartons
    total_accepted_cartons = accepted_cartons_per_customer * num_customers
    result = total_accepted_cartons
    return result

print(solution())