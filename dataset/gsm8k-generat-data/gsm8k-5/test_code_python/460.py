def solution():
    # Calculate the bonus percentage
    bonus_percentage = 10 / 100  # John's bonus was $10k on a $100k salary, so his bonus percentage is 10%

    # Calculate the bonus amount for this year
    bonus_amount = bonus_percentage * 200000  # John's salary this year is $200k, so his bonus would be 10% of that

    # Calculate John's total pay for this year
    total_pay = 200000 + bonus_amount

    result = total_pay
    return result

print(solution())