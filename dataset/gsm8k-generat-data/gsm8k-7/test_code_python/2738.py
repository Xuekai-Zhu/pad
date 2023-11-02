def solution():
    num_twenty_bills = 2
    twenty_bill_value = 20

    num_five_bills = 3
    five_bill_value = 5

    loose_change = 4.5

    cake_cost = 17.5

    # Calculate the total value of all the bills
    total_bills_value = (num_twenty_bills * twenty_bill_value) + (num_five_bills * five_bill_value)

    # Calculate the total amount of money before buying the cake
    total_money = total_bills_value + loose_change

    # Calculate the amount of money left after buying the cake
    money_left = total_money - cake_cost
    result = money_left
    return result

print(solution())