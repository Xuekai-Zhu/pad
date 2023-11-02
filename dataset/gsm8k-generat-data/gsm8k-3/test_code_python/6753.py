def solution():
    """Amanda has to sell 80 tickets in 3 days so she can make enough money to go on vacation. On the first day, she sells 5 of her friends 4 tickets each. On the second day she sells 32 tickets. How many tickets does she need to sell on the third day to meet her goal?"""
    # Define the total number of tickets Amanda needs to sell
    total_tickets = 80

    # Calculate the number of tickets Amanda sold on the first day
    first_day_tickets = 5 * 4

    # Calculate the number of tickets Amanda sold on the second day
    second_day_tickets = 32

    # Calculate the total number of tickets Amanda sold on the first two days
    sold_tickets = first_day_tickets + second_day_tickets

    # Calculate the number of tickets Amanda needs to sell on the third day
    third_day_tickets = total_tickets - sold_tickets

    # Display the number of tickets Amanda needs to sell on the third day
    result = third_day_tickets
    return result

print(solution())