def solution():
    hulk_height = 8 * 12 # Convert feet to inches
    hulk_weight = 1400
    elephant_carry_capacity = 19841
    if hulk_weight > elephant_carry_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())