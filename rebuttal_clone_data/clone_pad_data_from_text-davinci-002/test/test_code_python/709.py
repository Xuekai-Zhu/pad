def solution():
    initial_weight = 300
    weight_lost_month_one = 20
    weight_lost_month_two = weight_lost_month_one / 2
    weight_lost_month_three = weight_lost_month_two / 2
    weight_lost_month_four = weight_lost_month_three / 2
    weight_lost_month_five = (initial_weight - 250.5) - (weight_lost_month_one + weight_lost_month_two + weight_lost_month_three + weight_lost_month_four)
    result = weight_lost_month_five
    return result

print(solution())