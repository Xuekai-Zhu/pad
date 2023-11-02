def solution():
    """Mark goes into the store to buy some groceries. He buys 6 2$ cans of soup, 2 $5 loaves of bread, 2 3$ boxes of cereal, and 2 $4 gallons of milk. When he gets to the register, he opens his wallet to pay and realizes he only has $10 bills in there. How many $10 bills does he need to use to pay?"""
    # Define the prices of the items
    soup_price = 2
    bread_price = 5
    cereal_price = 3
    milk_price = 4

    # Calculate the total cost of the groceries
    total_cost = (6 * soup_price) + (2 * bread_price) + (2 * cereal_price) + (2 * milk_price)

    # Calculate the number of $10 bills needed to pay
    num_bills = total_cost // 10 + (total_cost % 10 > 0)

    # Return the result
    result = num_bills
    return result

print(solution())