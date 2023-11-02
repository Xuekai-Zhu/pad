def solution():
    """Wade has a hot dog food truck. He makes $2.00 in tips per customer. On Friday he served 28 customers. He served three times that amount of customers on Saturday. On Sunday, he served 36 customers. How many dollars did he make in tips between the 3 days?"""
    # Define the tips per customer
    TIPS_PER_CUSTOMER = 2.00

    # Calculate the number of customers on each day
    friday_customers = 28
    saturday_customers = friday_customers * 3
    sunday_customers = 36

    # Calculate the tips earned on each day
    friday_tips = friday_customers * TIPS_PER_CUSTOMER
    saturday_tips = saturday_customers * TIPS_PER_CUSTOMER
    sunday_tips = sunday_customers * TIPS_PER_CUSTOMER

    # Calculate the total tips earned over the weekend
    total_tips = friday_tips + saturday_tips + sunday_tips

    # return the result
    result = total_tips
    return result

print(solution())