def solution():
    # Calculate Tom's goals on the first day
    tom_first_day = 2 + 3

    # Calculate Tom's goals on the second day
    tom_second_day = 6

    # Calculate Gina's goals on the second day
    gina_second_day = tom_second_day - 2

    # Calculate Gina's total goals
    gina_total = 2 + gina_second_day

    # Calculate Tom's total goals
    tom_total = tom_first_day + tom_second_day

    result = (gina_total, tom_total)
    return result

print(solution())