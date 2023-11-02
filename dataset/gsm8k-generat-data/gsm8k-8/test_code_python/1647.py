def solution():
    # Calculate the total number of times Sarah saw her reflection in tall mirrors
    sarah_tall = 10 * 3 * 5

    # Calculate the total number of times Sarah saw her reflection in wide mirrors
    sarah_wide = 5 * 5 * 3

    # Calculate the total number of times Ellie saw her reflection in tall mirrors
    ellie_tall = 6 * 3 * 5

    # Calculate the total number of times Ellie saw her reflection in wide mirrors
    ellie_wide = 3 * 5 * 5

    # Calculate the total number of times Sarah and Ellie saw their reflections
    total_reflections = sarah_tall + sarah_wide + ellie_tall + ellie_wide
    result = total_reflections
    return result

print(solution())