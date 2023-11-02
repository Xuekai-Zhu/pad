def solution():
    # Define the number of lottery tickets and winning numbers on each ticket
    num_tickets = 3
    winning_numbers_per_ticket = 5

    # Calculate the total number of winning numbers
    total_winning_numbers = num_tickets * winning_numbers_per_ticket

    # Calculate the total amount won
    amount_won = total_winning_numbers * 20
    result = amount_won
    return result

print(solution())