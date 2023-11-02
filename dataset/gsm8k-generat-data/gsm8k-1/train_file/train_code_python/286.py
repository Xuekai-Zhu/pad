def solution():
    """Bran's tuition fee is $90. He does a part-time job that pays him $15 per month and he has a scholarship
    that takes care of 30% of his tuition fee. If he needs to pay his tuition fee within 3 months, how much does
    Bran still need to pay?"""
    tuition_fee = 90
    scholarship = 0.3
    months = 3
    part_time_job_pay = 15 * months
    tuition_after_scholarship = tuition_fee * (1 - scholarship)
    remaining_tuition = tuition_after_scholarship - part_time_job_pay
    result = remaining_tuition
    return result

print(solution())