def solution():
    """Brendan works online and is paid every week. Once he gets the money, he recharges his debit card with half of his pay. In June, he earned $5000 and bought himself a used car worth $1500. What is his total amount of remaining money at the end of the month?"""
    # Define the amount of money Brendan earned in June
    earnings = 5000

    # Calculate the amount of money Brendan put on his debit card each week
    weekly_recharge = earnings / 2 / 4

    # Calculate the total amount of money Brendan put on his debit card in June
    total_recharge = weekly_recharge * 4

    # Calculate the amount of money Brendan spent on the used car
    car_spending = 1500

    # Calculate Brendan's remaining money at the end of the month
    remaining_money = earnings - total_recharge - car_spending

    # return the result
    result = remaining_money
    return result

print(solution())