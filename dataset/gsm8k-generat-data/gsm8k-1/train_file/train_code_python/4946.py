def solution():
    """Tony bought 3 lottery tickets and chose identical numbers on each ticket. He finds out that 5 of the numbers on each lottery ticket are winning numbers. If each winning number is worth $20 then how much money, in dollars, has Tony won in total?"""
    tickets_bought = 3
    winning_numbers = 5
    prize_per_number = 20
    total_prize = tickets_bought * winning_numbers * prize_per_number
    result = total_prize
    return result

print(solution())