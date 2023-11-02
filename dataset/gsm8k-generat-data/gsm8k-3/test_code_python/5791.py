def solution():
    """Elroy decides to enter a walk-a-thon and wants to make sure he ties last year's winner's cash collection. Last year, walkers earned $4 a mile. This year walkers earn $2.75 a mile. If last year's winner collected $44, how many more miles will Elroy walk than last year's winner to collect the same amount of money?"""
    # Define the amount earned per mile for last year and this year
    LAST_YEAR_RATE = 4
    THIS_YEAR_RATE = 2.75

    # Define the amount collected by last year's winner
    LAST_YEAR_AMOUNT = 44

    # Calculate the number of miles last year's winner walked
    last_year_miles = LAST_YEAR_AMOUNT / LAST_YEAR_RATE

    # Calculate the number of miles Elroy needs to walk to collect the same amount of money
    elroy_miles = LAST_YEAR_AMOUNT / THIS_YEAR_RATE

    # Calculate the difference in miles between last year's winner and Elroy
    difference = elroy_miles - last_year_miles

    # Display the difference in miles
    result = difference
    return result

print(solution())