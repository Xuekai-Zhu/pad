def solution():
    """Lorie has 2 pieces of $100 bills. He requested to change one piece of the $100 bills into $50 bills. Half of the remaining $100 bill is changed to $10 bills while the rest is changed to $5 bills. How many pieces of bills will she have?"""
    # Define the initial amount of money
    initial_money = 2 * 100

    # Change one piece of $100 bills to $50 bills
    initial_money -= 100
    initial_money += 50

    # Change half of the remaining $100 bill to $10 bills
    remaining_money = initial_money - 50
    initial_money -= remaining_money / 2
    initial_money += (remaining_money / 2) / 10 * 10

    # Change the remaining money to $5 bills
    initial_money -= (remaining_money / 2) / 10 * 5
    initial_money += (remaining_money / 2) / 5 * 5

    # Calculate the number of pieces of bills
    number_of_bills = initial_money / 5

    # Display the number of pieces of bills
    result = number_of_bills
    return result

print(solution())