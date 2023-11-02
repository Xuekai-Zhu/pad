def solution():
    """Mark goes into the store to buy some groceries.  He buys 6 2$ cans of soup, 2 $5 loaves of bread, 2 3$ boxes of cereal, and 2 $4 gallons of milk.  When he gets to the register, he opens his wallet to pay and realizes he only has $10 bills in there.  How many $10 bills does he need to use to pay?"""
    # Calculate the total cost of all the items
    total_cost = (6 * 2) + (2 * 5) + (2 * 3) + (2 * 4)

    # Calculate the number of $10 bills needed to pay
    num_10_bills = total_cost // 10

    # Display the number of $10 bills needed to pay
    result = num_10_bills
    return result

print(solution())