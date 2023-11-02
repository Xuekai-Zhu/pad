def solution():
    """Wade has a hot dog food truck. He makes $2.00 in tips per customer. On Friday he served 28 customers. He served three times that amount of customers on Saturday. On Sunday, he served 36 customers. How many dollars did he make in tips between the 3 days?"""
    # Define the tips per customer
    TIPS_PER_CUSTOMER = 2.0

    # Calculate the number of customers Wade served on Friday
    friday_customers = 28

    # Calculate the number of customers Wade served on Saturday
    saturday_customers = 3 * friday_customers

    # Calculate the number of customers Wade served on Sunday
    sunday_customers = 36

    # Calculate the total tips Wade made
    total_tips = (friday_customers + saturday_customers + sunday_customers) * TIPS_PER_CUSTOMER

    # Display the total tips
    result = total_tips
    return result

print(solution())