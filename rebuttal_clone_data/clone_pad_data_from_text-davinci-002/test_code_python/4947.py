def solution():
    cost_per_ticket = 3
    winning_numbers = 5
    prize_per_winning_number = 20
    total_prize = winning_numbers * prize_per_winning_number
    final_prize = total_prize * cost_per_ticket
    result = final_prize
    return result

print(solution())