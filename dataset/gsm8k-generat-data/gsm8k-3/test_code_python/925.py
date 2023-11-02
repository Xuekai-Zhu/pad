def solution():
    """Ann, Becky, and Julia are working at a pharmacy, every day for 8 hours. Each of them is providing service to 7 customers per hour. One day Julia had to finish her work earlier, so she was working only for 6 hours. How many customers did all three of these women serve that day in total?"""
    # Define the number of hours each person worked
    ann_hours = 8
    becky_hours = 8
    julia_hours = 6

    # Define the number of customers each person serves per hour
    CUSTOMERS_PER_HOUR = 7

    # Calculate the total number of customers served by Ann and Becky
    total_customers = (ann_hours + becky_hours) * CUSTOMERS_PER_HOUR

    # Calculate the number of customers served by Julia
    julia_customers = julia_hours * CUSTOMERS_PER_HOUR

    # Calculate the total number of customers served by all three women
    total_customers += julia_customers

    # Display the total number of customers served
    result = total_customers
    return result

print(solution())