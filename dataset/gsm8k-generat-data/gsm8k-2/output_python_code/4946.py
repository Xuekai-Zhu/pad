def solution():
    """Tony bought 3 lottery tickets and chose identical numbers on each ticket. He finds out that 5 of the numbers on each lottery ticket are winning numbers. If each winning number is worth $20 then how much money, in dollars, has Tony won in total?"""
    num_tickets = 3
    num_winning_numbers = 5
    winnings_per_number = 20
    total_winnings = num_tickets * num_winning_numbers * winnings_per_number
    result = total_winnings
    return result

print(solution())