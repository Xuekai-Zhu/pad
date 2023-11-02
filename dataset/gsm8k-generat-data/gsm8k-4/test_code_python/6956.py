def solution():
    """Viggo spent $80 on a shirt. He paid the shirt using $20 and $10 bills. If she gave the clerk one more $20 bill than $10 bills, how many $10 bills did he give?"""
    # Define the total amount spent and the denominations of bills used
    total_spent = 80
    twenty_dollars = 0
    ten_dollars = 0

    # Use a loop to find the number of $20 and $10 bills
    while twenty_dollars <= ten_dollars + 1:
        # Increment the number of $20 bills
        twenty_dollars += 1
        # Calculate the remaining amount to be paid using $10 bills
        remaining_amount = total_spent - (twenty_dollars * 20)
        # Calculate the number of $10 bills needed to pay the remaining amount
        ten_dollars = remaining_amount // 10

    # Return the number of $10 bills
    result = ten_dollars
    return result

print(solution())