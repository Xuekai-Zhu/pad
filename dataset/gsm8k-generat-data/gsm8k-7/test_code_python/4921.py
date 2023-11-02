def solution():
    num_1_bills = 2
    num_5_bills = 1
    num_quarters = 13
    num_dimes = 20
    num_nickels = 8
    num_pennies = 35
    
    # Calculate the total value of all the bills
    total_bills_value = (num_1_bills * 1) + (num_5_bills * 5)
    
    # Calculate the total value of all the coins
    total_coins_value = (num_quarters * 0.25) + (num_dimes * 0.1) + (num_nickels * 0.05) + (num_pennies * 0.01)
    
    # Calculate the total amount of money Tyrone has
    total_money = total_bills_value + total_coins_value
    result = total_money
    return result

print(solution())