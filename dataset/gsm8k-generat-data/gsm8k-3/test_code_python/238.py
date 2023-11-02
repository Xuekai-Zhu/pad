def solution():
    """Jake has $5000. He spends $2800 on a new motorcycle, and then spends half of what's left on a concert ticket. Jake then loses a fourth of what he has left. How much money does he have left?"""
    # Define Jake's initial amount of money
    jake_money = 5000

    # Subtract the cost of the motorcycle
    jake_money -= 2800

    # Calculate the cost of the concert ticket
    concert_ticket_cost = jake_money / 2

    # Subtract the cost of the concert ticket
    jake_money -= concert_ticket_cost

    # Calculate the amount lost
    lost_money = jake_money / 4

    # Subtract the lost money
    jake_money -= lost_money

    # Display the amount of money Jake has left
    result = jake_money
    return result

print(solution())