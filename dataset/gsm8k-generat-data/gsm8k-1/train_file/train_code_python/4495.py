def solution():
    """Sabina is starting her first year of college that costs $30,000. She has saved $10,000 for her first year. She was awarded a grant that will cover 40% of the remainder of her tuition. How much will Sabina need to apply for to receive a loan that will cover her tuition?"""
    total_tuition = 30000
    savings = 10000
    remaining_tuition = total_tuition - savings
    grant_percent = 40
    grant_amount = remaining_tuition * (grant_percent / 100)
    loan_amount = remaining_tuition - grant_amount
    result = loan_amount
    return result

print(solution())