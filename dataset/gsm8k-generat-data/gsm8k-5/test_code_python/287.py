def solution():
    tuition_fee = 90  # Bran's tuition fee is $90
    scholarship = tuition_fee * 0.3  # Bran's scholarship covers 30% of his tuition fee
    remaining_fee = tuition_fee - scholarship  # Bran still needs to pay the remaining fee
    part_time_income = 15 * 3  # Bran's part-time job pays him $15 per month, for 3 months
    amount_due = remaining_fee - part_time_income  # Bran still needs to pay the remaining fee, after deducting his part-time income

    result = amount_due
    return result

print(solution())