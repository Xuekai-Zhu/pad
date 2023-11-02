def solution():
    """Mark goes into the store to buy some groceries. He buys 6 2$ cans of soup, 2 $5 loaves of bread, 2 3$ boxes of cereal, and 2 $4 gallons of milk. When he gets to the register, he opens his wallet to pay and realizes he only has $10 bills in there. How many $10 bills does he need to use to pay?"""
    soup_cost = 6 * 2
    bread_cost = 2 * 5
    cereal_cost = 2 * 3
    milk_cost = 2 * 4
    total_cost = soup_cost + bread_cost + cereal_cost + milk_cost
    num_bills = total_cost / 10
    result = num_bills
    return result

print(solution())