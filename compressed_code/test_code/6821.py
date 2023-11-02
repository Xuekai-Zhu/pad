def solution():
    
    oyster_price = 15
    shrimp_price = 14
    clams_price = 13.5
    oyster_dozen = 3
    shrimp_pounds = 2
    clams_pounds = 2
    total_oyster_price = oyster_price * oyster_dozen
    total_shrimp_price = shrimp_price * shrimp_pounds
    total_clams_price = clams_price * clams_pounds
    total_price = total_oyster_price + total_shrimp_price + total_clams_price
    split_bill = total_price / 4
    result = split_bill
    return result

print(solution())