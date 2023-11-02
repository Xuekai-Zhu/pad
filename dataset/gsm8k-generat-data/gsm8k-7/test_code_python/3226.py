def solution():
    friday_customers = 28
    saturday_customers = friday_customers * 3
    sunday_customers = 36
    tip_amount = 2

    # Calculate the total tips collected on Friday
    friday_tips = friday_customers * tip_amount

    # Calculate the total tips collected on Saturday
    saturday_tips = saturday_customers * tip_amount

    # Calculate the total tips collected on Sunday
    sunday_tips = sunday_customers * tip_amount

    # Calculate the total tips collected over the three days
    total_tips = friday_tips + saturday_tips + sunday_tips
    result = total_tips
    return result

print(solution())