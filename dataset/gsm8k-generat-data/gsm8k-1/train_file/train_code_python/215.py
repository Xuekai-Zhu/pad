def solution():
    """Missy had a giant piggy bank in her bedroom. Every day she would search the house for change to put in her bank. After 4 years, the bank was opened and it contained $450 in change. If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?"""
    total_money = 450
    fourth_year = total_money/15
    third_year = fourth_year/2
    second_year = third_year/2
    first_year = total_money - (fourth_year+third_year+second_year)
    result = first_year
    return result

print(solution())