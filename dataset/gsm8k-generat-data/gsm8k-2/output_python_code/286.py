def solution():
    """Bran's tuition fee is $90. He does a part-time job that pays him $15 per month and he has a scholarship that takes care of 30% of his tuition fee. If he needs to pay his tuition fee within 3 months, how much does Bran still need to pay?"""
    tuition_fee = 90
    part_time_pay = 15
    scholarship_percent = 0.3
    scholarship_amount = tuition_fee * scholarship_percent
    remaining_tuition_fee = tuition_fee - scholarship_amount
    remaining_tuition_fee -= part_time_pay * 3
    result = remaining_tuition_fee
    return result

print(solution())