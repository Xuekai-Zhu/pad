def solution():
    extra_cans = 5
    total_cans = 33
    cans_per_customer_per_day = 2

    # Calculate the total number of hairspray cans used by all customers in a day
    total_customer_cans = total_cans - extra_cans

    # Calculate the number of customers that come to the salon each day
    num_customers = total_customer_cans / cans_per_customer_per_day
    result = num_customers
    return result

print(solution())