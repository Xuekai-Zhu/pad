def solution():
    two_hundred_bills = 2
    one_hundred_bill = 1
    fifty_bill = 1
    twenty_bill = 5
    ten_bill = 3
    five_bill = 7
    one_bill = 27
    total_bills = two_hundred_bills + one_hundred_bill + fifty_bill + twenty_bill + \
                 ten_bill + five_bill + one_bill
    coins = 0
    total_amount = total_bills + coins
    result = 300 - total_amount
    return result

print(solution())