def solution():
    """Missy had a giant piggy bank in her bedroom.  Every day she would search the house for change to put in her bank.  After 4 years, the bank was opened and it contained $450 in change.  If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?"""
    # Initialize the total amount of money Missy put in the bank
    total_amount = 450

    # Calculate the amount of money Missy put in the bank in the fourth year
    fourth_year_amount = total_amount / 15

    # Calculate the amount of money Missy put in the bank in the third year
    third_year_amount = fourth_year_amount / 2

    # Calculate the amount of money Missy put in the bank in the second year
    second_year_amount = third_year_amount / 2

    # Calculate the amount of money Missy put in the bank in the first year
    first_year_amount = total_amount - (fourth_year_amount + third_year_amount + second_year_amount)

    # Display the amount of money Missy put in the bank in the first year
    result = first_year_amount
    return result

print(solution())