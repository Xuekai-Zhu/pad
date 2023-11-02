def solution():
    initial_lift = 135
    increase_lift = 265
    percent_increase = 600
    increase_amount = (initial_lift + increase_lift) * (percent_increase / 100)
    total_lift = initial_lift + increase_lift + increase_amount
    result = total_lift
    return result

print(solution())