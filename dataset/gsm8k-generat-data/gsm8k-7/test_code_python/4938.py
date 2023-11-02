def solution():
    num_cartons = 400
    num_customers = 4
    num_damaged_cartons_per_customer = 60

    # Calculate the total number of cartons delivered to all customers
    total_delivered_cartons = num_cartons * num_customers

    # Calculate the total number of damaged cartons
    total_damaged_cartons = num_customers * num_damaged_cartons_per_customer

    # Calculate the total number of accepted cartons
    total_accepted_cartons = total_delivered_cartons - total_damaged_cartons
    result = total_accepted_cartons
    return result

print(solution())