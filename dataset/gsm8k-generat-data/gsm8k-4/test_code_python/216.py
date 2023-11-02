def solution():
    """Missy had a giant piggy bank in her bedroom. Every day she would search the house for change to put in her bank. After 4 years, the bank was opened and it contained $450 in change. If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?"""
    # Define the total amount in the piggy bank
    total_amount = 450

    # Define the variable for the money put in the bank during the first year
    first_year_amount = None

    # Calculate the amount of money put in the bank during the fourth year
    fourth_year_amount = total_amount / 15

    # Calculate the amount of money put in the bank during the third year
    third_year_amount = fourth_year_amount / 2

    # Calculate the amount of money put in the bank during the second year
    second_year_amount = third_year_amount / 2

    # Calculate the amount of money put in the bank during the first year
    first_year_amount = total_amount - (fourth_year_amount + third_year_amount + second_year_amount)

    result = first_year_amount
    return result

print(solution())