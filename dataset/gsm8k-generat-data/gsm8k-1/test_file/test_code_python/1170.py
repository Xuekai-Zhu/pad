def solution():
    """Thomas withdraws $1000 in 20 dollar bills from the bank account. He loses 10 bills while getting home. After that, he uses half of the remaining bills to pay for a bill. Thomas then triples his money. He then converts all his bills to 5 dollar bills. How many 5 dollar bills does he have?"""
    num_twenty_bills = 50
    lost_bills = 10
    remaining_bills = num_twenty_bills - lost_bills
    remaining_bills_after_payment = remaining_bills // 2
    starting_money = num_twenty_bills * 20
    money_after_payment = remaining_bills_after_payment * 20
    tripled_money = starting_money - money_after_payment
    num_five_bills = tripled_money // 5
    result = num_five_bills
    return result

print(solution())