def solution():
    num_hours = 8
    num_customers_per_hour = 7

    # Calculate the total number of customers each woman served
    ann_customers = num_hours * num_customers_per_hour
    becky_customers = num_hours * num_customers_per_hour
    julia_customers = 6 * num_customers_per_hour

    # Calculate the total number of customers all three women served
    total_customers = ann_customers + becky_customers + julia_customers
    result = total_customers
    return result

print(solution())