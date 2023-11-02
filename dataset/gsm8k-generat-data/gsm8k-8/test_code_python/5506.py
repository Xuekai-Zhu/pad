def solution():
    # Find the capacity of one tank
    capacity = 450 / 0.45

    # Find how much water is needed to fill the first tank
    first_tank_needed = capacity - 300

    # Find how much water is needed to fill the second tank
    second_tank_needed = capacity - (0.45 * capacity)

    # Find the total water needed to fill both tanks
    total_needed = first_tank_needed + second_tank_needed

    result = total_needed
    return result

print(solution())