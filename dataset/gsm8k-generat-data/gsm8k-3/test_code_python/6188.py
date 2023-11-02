def solution():
    """Dino does some online gig work for a living.  He works 20 hours a month making $10 an hour.  He works 30 hours a month making $20 an hour.  He works 5 hours a month making $40 an hour.  He pays $500 a month in expenses.  How much money does Dino have left at the end of the month?"""
    # Calculate Dino's total earnings from each type of gig work
    first_gig_earnings = 20 * 10
    second_gig_earnings = 30 * 20
    third_gig_earnings = 5 * 40

    # Calculate Dino's total earnings for the month
    total_earnings = first_gig_earnings + second_gig_earnings + third_gig_earnings

    # Calculate Dino's total expenses for the month
    total_expenses = 500

    # Calculate Dino's money left at the end of the month
    money_left = total_earnings - total_expenses

    # Display Dino's money left
    result = money_left
    return result

print(solution())