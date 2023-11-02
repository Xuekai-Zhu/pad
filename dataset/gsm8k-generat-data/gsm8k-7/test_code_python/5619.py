def solution():
    num_100_bills = 2
    num_50_bills = 1
    num_20_bills = 5
    num_10_bills = 3
    num_5_bills = 7
    num_1_bills = 27

    # Calculate the total value of all the bills
    total_bills_value = (num_100_bills * 100) + (num_50_bills * 50) + (num_20_bills * 20) + (num_10_bills * 10) + (num_5_bills * 5) + num_1_bills

    # Calculate the value of the coins
    # It is not specified how many coins there are, so we cannot solve this problem

    # Calculate the amount of money that Jack will hand in
    amount_to_hand_in = total_bills_value - 300
    result = amount_to_hand_in
    return result

print(solution())