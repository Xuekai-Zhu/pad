def solution():
    """Reese had a sum of money in her savings account. The company she used to work with was not doing well which is why she lost her job. So she spent 20% of her savings for her expenses in February, 40% of it in March, and $1500 in April. How much did she have in her savings account if she still has $2900 after spending those amounts?"""
    # Define the percentage of savings spent in February and March
    FEB_SPENT = 0.2
    MAR_SPENT = 0.4

    # Define the amount spent in April
    APR_SPENT = 1500

    # Define the remaining amount in the savings account
    remaining = 2900

    # Calculate the total amount before spending
    total_before = remaining + APR_SPENT

    # Calculate the amount spent in March
    mar_spent = MAR_SPENT * total_before

    # Calculate the amount before spending in March
    total_before_mar = total_before + mar_spent

    # Calculate the amount spent in February
    feb_spent = FEB_SPENT * total_before_mar

    # Calculate the initial amount in the savings account
    initial = total_before_mar + feb_spent

    # Display the initial amount
    result = initial
    return result

print(solution())