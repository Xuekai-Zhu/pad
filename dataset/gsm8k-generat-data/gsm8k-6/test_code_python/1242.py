def solution():
    # Calculate Vinny's weight after the first month
    weight_after_month_1 = 300 - 20 

    # Calculate the weight Vinny lost in the second, third, and fourth months
    weight_lost_month_2 = (1/2) * 20
    weight_lost_month_3 = (1/2) * weight_lost_month_2
    weight_lost_month_4 = (1/2) * weight_lost_month_3

    # Calculate Vinny's weight at the start of the fifth month
    weight_start_month_5 = weight_after_month_1 - weight_lost_month_2 - weight_lost_month_3 - weight_lost_month_4

    # Calculate the extra weight Vinny lost in the fifth month
    extra_weight_lost_month_5 = weight_start_month_5 - 250.5

    result = extra_weight_lost_month_5
    return result

print(solution())