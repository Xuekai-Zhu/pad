def solution():
    one_bills = 2
    five_bills = 1
    quarters = 13
    dimes = 20
    nickels = 8
    pennies = 35
    value_of_one_bill = 100
    value_of_five_bill = 500
    value_of_quarter = 25
    value_of_dime = 10
    value_of_nickel = 5
    value_of_penny = 1
    total_value = (one_bills * value_of_one_bill) + (five_bills * value_of_five_bill) + (quarters * value_of_quarter) + (dimes * value_of_dime) + (nickels * value_of_nickel) + (pennies * value_of_penny)
    result = total_value
    
    return result

print(solution())