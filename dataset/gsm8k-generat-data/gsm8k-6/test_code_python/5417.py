def solution():
    # Calculate Mary's weight after each stage of the diet
    initial_weight = 99
    first_drop = initial_weight - 12
    second_gain = first_drop + (2 * 12)
    third_drop = second_gain - (3 * 12)
    final_gain = third_drop + 6

    result = final_gain
    return result

print(solution())