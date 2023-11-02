def solution():
    """Steve wanted to make a total of $100 within four days, so he took on a berry-picking job in Sweden. The job paid $2 for every pound of lingonberries picked. On Monday he picked 8 pounds. Tuesday’s harvest was triple what he had picked the previous day. On Wednesday he felt very tired and decided to rest. How many pounds of lingonberries did Steve have to pick on Thursday?"""
    # Define the amount of money Steve wants to make and the rate of pay per pound of lingonberries picked
    TARGET_AMOUNT = 100
    PAY_RATE = 2

    # Calculate the amount of money Steve earned on Monday
    monday_earnings = 8 * PAY_RATE

    # Calculate the amount of money Steve earned on Tuesday
    tuesday_earnings = 3 * 8 * PAY_RATE

    # Calculate the total amount of money Steve earned in the first two days
    total_earnings = monday_earnings + tuesday_earnings

    # Calculate the amount of money Steve still needs to earn
    remaining_earnings = TARGET_AMOUNT - total_earnings

    # Calculate the amount of lingonberries Steve needs to pick on Thursday to earn the remaining amount of money
    thursday_pounds = remaining_earnings / PAY_RATE

    # Display the pounds of lingonberries Steve needs to pick on Thursday
    result = thursday_pounds
    return result

print(solution())