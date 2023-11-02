def solution():
    """At Peanut Emporium, peanuts cost $3 per pound with a 15-pound minimum. If Baxter spent $105 on peanuts, how many pounds over the minimum did he purchase?"""
    # Define the cost per pound and minimum purchase
    COST_PER_POUND = 3
    MINIMUM_PURCHASE = 15

    # Calculate the total number of pounds Baxter bought
    total_pounds = int(105 / COST_PER_POUND)

    # Calculate the number of pounds over the minimum
    pounds_over_minimum = max(0, total_pounds - MINIMUM_PURCHASE)

    # Display the pounds over the minimum
    result = pounds_over_minimum
    return result

print(solution())