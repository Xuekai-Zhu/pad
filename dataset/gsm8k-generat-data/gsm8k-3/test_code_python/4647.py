def solution():
    """Monica was saving money for her future. Every week he put $15 into her moneybox. After the moneybox got full, which took 60 weeks, Monica took all the money out and took it to the bank, and she started saving money again. She repeated this whole process 5 times. How much money did Monica take to the bank in total?"""
    # Define the amount saved each week and the number of weeks until the moneybox is full
    WEEKLY_SAVINGS = 15
    WEEKS_TO_FILL = 60

    # Calculate the total amount saved in one cycle
    cycle_savings = WEEKLY_SAVINGS * WEEKS_TO_FILL

    # Calculate the total amount saved over 5 cycles
    total_savings = cycle_savings * 5

    # Display the total amount saved
    result = total_savings
    return result

print(solution())