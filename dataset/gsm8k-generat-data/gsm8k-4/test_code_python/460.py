def solution():
    """John gets a bonus that's the same percentage every year. Last year he made $100,000 and got a $10,000 bonus. This year he makes $200,000. How much will John make this year when adding both his total pay and bonus together?"""
    # Calculate the bonus percentage
    bonus_percentage = 10000 / 100000

    # Calculate this year's potential bonus
    potential_bonus = bonus_percentage * 200000

    # Calculate John's total pay and bonus for this year
    total_pay = 200000 + potential_bonus

    result = total_pay
    return result

print(solution())