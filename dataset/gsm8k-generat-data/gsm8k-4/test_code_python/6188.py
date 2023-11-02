def solution():
    """Dino does some online gig work for a living. He works 20 hours a month making $10 an hour. He works 30 hours a month making $20 an hour. He works 5 hours a month making $40 an hour. He pays $500 a month in expenses. How much money does Dino have left at the end of the month?"""
    # Calculate the earnings from each type of work
    work1_earnings = 20 * 10
    work2_earnings = 30 * 20
    work3_earnings = 5 * 40

    # Calculate the total earnings
    total_earnings = work1_earnings + work2_earnings + work3_earnings

    # Subtract the expenses
    total_earnings -= 500

    # return the result
    result = total_earnings
    return result

print(solution())