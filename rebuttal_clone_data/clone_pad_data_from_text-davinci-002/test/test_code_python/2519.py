def solution():
    cost_per_bottle = 2
    glasses_per_bottle = 5
    glasses_consumed_per_night = 1
    number_of_nights = 365
    total_cost = cost_per_bottle * (glasses_consumed_per_night / glasses_per_bottle) * number_of_nights
    result = total_cost
    return result

print(solution())