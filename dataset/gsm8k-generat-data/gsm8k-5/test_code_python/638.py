def solution():
    # Calculate the total amount spent on lotto tickets
    total_spent = 200 * 2  # James buys 200 tickets for $2 each

    # Calculate the total number of winning tickets
    total_winners = 0.2 * 200  # 20% of 200 tickets are winners

    # Calculate the total amount won from $5 winners
    total_5_winners = 0.8 * total_winners  # 80% of winners win $5
    total_won_5 = total_5_winners * 5

    # Calculate the total amount won, including the grand prize and average $10 winnings
    total_won = total_won_5 + 5000 + total_winners * 10

    # Calculate James' profit
    profit = total_won - total_spent

    result = profit
    return result

print(solution())