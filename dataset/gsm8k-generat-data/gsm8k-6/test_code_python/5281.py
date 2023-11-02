def solution():
    # Calculate the total amount saved by the couple in 6 months
    total_saved = (335 + 225) * 4 * 6  # husband saves $335/week and wife saves $225/week for 6 months

    # Calculate half of the couple's total savings
    half_savings = total_saved / 2

    # Calculate the amount each child receives
    each_child = half_savings / 4

    result = each_child
    return result

print(solution())