def solution():
    # Calculate the total amount of money made from sales of pumpkin pie
    pumpkin_pieces = 8 * 4  # There are 8 pieces in each pumpkin pie, and Teal sold 4 pumpkin pies
    pumpkin_sales = pumpkin_pieces * 5  # Each slice of pumpkin pie sells for $5
    # Calculate the total amount of money made from sales of custard pie
    custard_pieces = 6 * 5  # There are 6 pieces in each custard pie, and Teal sold 5 custard pies
    custard_sales = custard_pieces * 6  # Each slice of custard pie sells for $6
    # Calculate the total amount of money made from both types of pies
    total_sales = pumpkin_sales + custard_sales
    result = total_sales
    return result

print(solution())