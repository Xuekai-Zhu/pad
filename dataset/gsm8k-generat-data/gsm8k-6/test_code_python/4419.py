def solution():
    # Calculate the total cost of Mark's groceries
    total_cost = 6*2 + 2*5 + 2*3 + 2*4  # cost of 6 cans of soup, 2 loaves of bread, 2 boxes of cereal, and 2 gallons of milk
    # Calculate the number of $10 bills Mark needs to use
    num_bills = total_cost // 10  # integer division to get the number of $10 bills needed
    if total_cost % 10 != 0:  # if there is a remainder, Mark needs one more $10 bill
        num_bills += 1
    result = num_bills
    return result

print(solution())