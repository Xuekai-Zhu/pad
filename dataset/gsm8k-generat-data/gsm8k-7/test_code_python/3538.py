def solution():
    day1_distance = 135
    day2_distance = 135 + 124
    day3_distance = 135 + 124 + 159
    day4_distance = 135 + 124 + 159 + 189
    total_distance = day1_distance + day2_distance + day3_distance + day4_distance

    phone_charge_distance = 106
    num_phone_charges = total_distance // phone_charge_distance

    result = num_phone_charges
    return result

print(solution())