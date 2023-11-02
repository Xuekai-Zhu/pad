def solution():
    """Ellie and Sarah got lost in a house of mirrors and discuss how many times they've seen their own reflections. 
    They both passed through the room with tall mirrors 3 times each and the room with wide mirrors 5 times each.
    Sarah saw her reflection 10 times in the tall mirrors and 5 times in the wide mirrors. 
    Ellie saw her reflection 6 times in the tall mirrors and 3 times in the wide mirrors. 
    In total, how many times did Sarah and Ellie see their reflections?"""
    # Calculate the total number of reflections for Sarah
    tall_reflections_S = 3 * 10 + 5 * 5
    wide_reflections_S = 3 * 5 + 5 * 5
    total_reflections_S = tall_reflections_S + wide_reflections_S

    # Calculate the total number of reflections for Ellie
    tall_reflections_E = 3 * 6 + 5 * 0
    wide_reflections_E = 3 * 0 + 5 * 3
    total_reflections_E = tall_reflections_E + wide_reflections_E

    # Calculate the total number of reflections for both of them
    total_reflections = total_reflections_S + total_reflections_E

    # return the result
    return total_reflections

print(solution())