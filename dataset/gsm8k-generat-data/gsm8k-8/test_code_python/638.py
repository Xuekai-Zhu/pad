def solution():
    # Calculate the total cost of the lotto tickets
    total_cost = 200 * 2

    # Calculate the number of winning tickets
    num_winners = 0.2 * 200

    # Calculate the total winnings from the $5 winners
    total_5_winners = 0.8 * num_winners * 5

    # Calculate the total winnings from the other winners
    total_other_winners = ((1/num_winners) - 0.8) * num_winners * 10

    # Calculate the total winnings
    total_winnings = total_5_winners + 5000 + total_other_winners

    # Calculate the profit
    profit = total_winnings - total_cost

    result = profit
    return result

print(solution())