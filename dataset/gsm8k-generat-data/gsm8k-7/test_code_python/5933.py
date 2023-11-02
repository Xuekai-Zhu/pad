def solution():
    num_20_bills = 10
    num_10_bills = 8
    num_5_bills = 4
    bill_values = [20, 10, 5]

    # Calculate the total value of all bills
    total_value = (num_20_bills * 20) + (num_10_bills * 10) + (num_5_bills * 5)

    # Calculate the number of $100 bills that Marly will have
    num_100_bills = total_value // 100

    result = num_100_bills
    return result

print(solution())