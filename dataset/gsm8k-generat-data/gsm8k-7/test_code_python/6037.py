def solution():
    num_bills = 3
    value_per_bill = 20

    # Calculate the total value of the bills
    total_bills_value = num_bills * value_per_bill

    # Calculate James' total money after finding the bills
    total_money = total_bills_value + 75

    result = total_money
    return result

print(solution())