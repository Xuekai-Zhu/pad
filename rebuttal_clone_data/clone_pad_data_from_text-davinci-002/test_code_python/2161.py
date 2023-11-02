def solution():
    original_amount = 10
    donation = 4
    winnings = 90
    losses = 50 + 10 + 5
    cost_of_water = 1
    cost_of_ticket = 1
    winnings_from_ticket = 65
    final_amount = original_amount - donation + winnings - losses + winnings_from_ticket - cost_of_water - cost_of_ticket
    result = final_amount
    return result

print(solution())