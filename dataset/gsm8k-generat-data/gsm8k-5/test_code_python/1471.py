def solution():
    total = 120  # The total amount in the class fund is $120
    num_10_bills = 0  # Number of $10 bills
    num_20_bills = 0  # Number of $20 bills

    # Let's use a loop to check all possible combinations of $10 and $20 bills
    for i in range(1, 7):  # We know there are at most 6 $20 bills (to reach $120)
        num_20_bills = i
        num_10_bills = 2 * num_20_bills  # Number of $10 bills is twice the number of $20 bills
        if num_10_bills * 10 + num_20_bills * 20 == total:  # Check if the total amount matches
            result = num_20_bills
            return result

print(solution())