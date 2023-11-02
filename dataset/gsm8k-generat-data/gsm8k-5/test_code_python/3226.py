def solution():
    # Calculate tips earned on Friday
    friday_tips = 2 * 28  # $2.00 in tips per customer, 28 customers on Friday

    # Calculate tips earned on Saturday
    saturday_customers = 3 * 28  # Three times as many customers as Friday
    saturday_tips = 2 * saturday_customers  # $2.00 in tips per customer on Saturday

    # Calculate tips earned on Sunday
    sunday_tips = 2 * 36  # $2.00 in tips per customer, 36 customers on Sunday

    # Calculate total tips earned over the three days
    total_tips = friday_tips + saturday_tips + sunday_tips
    result = total_tips
    return result

print(solution())