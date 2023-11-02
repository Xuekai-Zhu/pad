def solution():
    """Missy had a giant piggy bank in her bedroom. Every day she would search the house for change to put in her bank. After 4 years, the bank was opened and it contained $450 in change. If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?"""
    total_change = 450
    fourth_year_change = total_change / 2
    third_year_change = fourth_year_change / 2
    second_year_change = third_year_change / 2
    first_year_change = total_change - (fourth_year_change + third_year_change + second_year_change)
    result = first_year_change
    return result

print(solution())