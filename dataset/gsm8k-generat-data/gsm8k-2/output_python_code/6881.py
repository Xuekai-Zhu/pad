def solution():
    """Brendan works online and is paid every week. Once he gets the money, he recharges his debit card with half of his pay. In June, he earned $5000 and bought himself a used car worth $1500. What is his total amount of remaining money at the end of the month?"""
    weekly_pay = 5000/4
    debit_card_amount = weekly_pay/2
    remaining_balance = (4*debit_card_amount) - 1500
    result = remaining_balance
    return result

print(solution())