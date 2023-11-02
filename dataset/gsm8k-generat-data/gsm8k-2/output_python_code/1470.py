def solution():
    """Karen's class fund contains only $10 and $20 bills, which amount to $120. The number of $10 bills is twice as many $20 bills. How many $20 bills do they have in their fund?"""
    total_amount = 120
    ten_bill_count = 0
    twenty_bill_count = 0

    # Start with assumption that there are 0 $20 bills and find how many $10 bills are needed
    while (twenty_bill_count * 20) <= total_amount:
        ten_bill_count = 2 * twenty_bill_count
        if (ten_bill_count * 10) + (twenty_bill_count * 20) == total_amount:
            result = twenty_bill_count
            return result
        twenty_bill_count += 1

    # If no solution is found, return None
    return None

print(solution())