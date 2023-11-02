def solution():
    """Emma has saved $230 in her bank account. She withdrew $60 to buy a new pair of shoes.
    The next week, she deposited twice as much money as she withdrew. How much is in her bank account now?"""
    starting_balance = 230
    shoe_purchase = 60
    withdrawal = shoe_purchase
    deposit = withdrawal * 2
    ending_balance = starting_balance - withdrawal + deposit
    result = ending_balance
    return result

print(solution())