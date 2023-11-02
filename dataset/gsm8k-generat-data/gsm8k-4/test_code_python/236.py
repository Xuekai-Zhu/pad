def solution():
    """Jake has $5000. He spends $2800 on a new motorcycle, and then spends half of what's left on a concert ticket. Jake then loses a fourth of what he has left. How much money does he have left?"""
    # Define the initial amount of money
    initial_money = 5000

    # Calculate the amount spent on the motorcycle
    spent_on_motorcycle = 2800

    # Calculate the amount of money left after buying the motorcycle
    money_left = initial_money - spent_on_motorcycle

    # Calculate the amount spent on the concert ticket
    spent_on_concert = money_left / 2

    # Calculate the amount of money left after buying the concert ticket
    money_left = money_left - spent_on_concert

    # Calculate the amount lost
    lost_money = money_left / 4

    # Calculate the amount of money left
    money_left = money_left - lost_money

    result = money_left
    return result

print(solution())