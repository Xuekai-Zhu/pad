def solution():
    num_wolves = 4
    num_additional_wolves = 16
    num_wolves_total = num_wolves + num_additional_wolves
    pounds_of_meat_per_wolf_per_day = 8
    days_without_hunting = 5
    pounds_of_meat_needed = num_wolves_total * pounds_of_meat_per_wolf_per_day * days_without_hunting

    pounds_of_meat_per_deer = 200
    num_deer_needed = pounds_of_meat_needed / pounds_of_meat_per_deer
    result = num_deer_needed / num_wolves_total
    return result

print(solution())