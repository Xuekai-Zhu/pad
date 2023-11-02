def solution():
    """Bran's tuition fee is $90. He does a part-time job that pays him $15 per month and he has a scholarship that takes care of 30% of his tuition fee. If he needs to pay his tuition fee within 3 months, how much does Bran still need to pay?"""
    # Define the tuition fee and the part-time job income
    tuition_fee = 90
    job_income = 15

    # Calculate the scholarship amount
    scholarship = tuition_fee * 0.3

    # Calculate the remaining tuition fee after the scholarship
    remaining_tuition = tuition_fee - scholarship

    # Calculate the total income from the part-time job
    total_income = job_income * 3

    # Calculate the amount still owed
    amount_owed = remaining_tuition - total_income

    # return the result
    result = amount_owed
    return result

print(solution())