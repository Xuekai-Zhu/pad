def solution():
    """Viggo spent $80 on a shirt. He paid the shirt using $20 and $10 bills. If she gave the clerk one more $20 bill than $10 bills, how many $10 bills did he give?"""
    # Let x be the number of $10 bills Viggo gave
    x = 0

    # Calculate the number of $20 bills giving
    y = x + 1

    # Calculate the total amount of money paid by adding the values of the bills
    total_money = x*10 + y*20

    # Check if the total amount matches the cost of the shirt
    while total_money != 80:
        x += 1
        y = x + 1
        total_money = x*10 + y*20

    # Display the number of $10 bills given
    result = x
    return result

print(solution())