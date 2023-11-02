def solution():
    tickets = 3  # Tony bought 3 lottery tickets
    numbers_per_ticket = 5  # Tony has 5 winning numbers on each ticket
    value_per_number = 20  # Each winning number is worth $20

    # Calculate the total amount of money won by Tony
    total_winnings = tickets * numbers_per_ticket * value_per_number
    result = total_winnings
    return result

print(solution())