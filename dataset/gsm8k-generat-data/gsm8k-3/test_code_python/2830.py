def solution():
    """Derek finally gets his own allowance. He puts $2 away in January, $4 away in February, $8 away in March, $16 away in April and follows this savings pattern through to December. How much money does he have to spare and save by December?"""
    # Define the initial savings amount and the savings pattern multiplier
    savings = 2
    multiplier = 2

    # Loop through the remaining months and add to the savings each time
    for month in range(2, 13):
        savings += savings * multiplier

    # Display the total savings
    result = savings
    return result

print(solution())