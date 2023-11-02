def solution():
    """Bran's tuition fee is $90. He does a part-time job that pays him $15 per month and he has a scholarship that takes care of 30% of his tuition fee. If he needs to pay his tuition fee within 3 months, how much does Bran still need to pay?"""
    tuition_fee = 90
    job_payment = 15
    scholarship = 30
    tuition_fee_remaining = tuition_fee - (tuition_fee * (scholarship / 100))
    monthly_payment = tuition_fee_remaining / 3
    result = monthly_payment
    return result

print(solution())