def solution():
    num_100_bills = 2

    # Change one $100 bill to $50 bills
    num_50_bills = 1
    remaining_money = 100

    # Change half of the remaining $100 bill to $10 bills
    num_10_bills = remaining_money // 2 // 10
    remaining_money -= num_10_bills * 10

    # Change the rest to $5 bills
    num_5_bills = remaining_money // 5

    # Calculate the total number of bills
    total_bills = num_100_bills + num_50_bills + num_10_bills + num_5_bills
    result = total_bills
    return result

print(solution())