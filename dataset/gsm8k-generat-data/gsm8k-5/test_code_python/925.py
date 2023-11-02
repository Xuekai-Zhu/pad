def solution():
    hours_worked = [8, 8, 6]  # Ann and Becky worked for 8 hours, Julia worked for only 6 hours
    customers_per_hour = 7  # Each woman provides service to 7 customers per hour

    # Calculate the total number of customers served by each woman
    customers_served = [hours * customers_per_hour for hours in hours_worked]

    # Calculate the total number of customers served by all three women
    total_customers = sum(customers_served)
    result = total_customers
    return result

print(solution())