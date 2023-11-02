def solution():
    """Brendan works online and is paid every week. Once he gets the money, he recharges his debit card with half of his pay. In June, he earned $5000 and bought himself a used car worth $1500. What is his total amount of remaining money at the end of the month?"""
    # Calculate the amount of money Brendan recharged on his debit card
    recharge_amount = (5000 / 2)

    # Calculate his remaining balance after buying the used car
    remaining_balance = recharge_amount - 1500

    # Display his remaining balance
    result = remaining_balance
    return result

print(solution())