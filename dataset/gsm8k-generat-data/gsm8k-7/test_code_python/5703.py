def solution():
    price_per_hamburger = 5
    customers = [(4, 2), (2, 2)]
    total_hamburgers = 0

    # Calculate the total number of hamburgers purchased by all customers
    for customer in customers:
        total_hamburgers += sum(customer)

    # Calculate the total revenue generated by all hamburgers sold
    total_revenue = total_hamburgers * price_per_hamburger
    
    # Calculate the number of hamburgers Frank needs to sell to make $50
    hamburgers_needed = (50 - total_revenue) // price_per_hamburger
    
    result = hamburgers_needed
    return result

print(solution())