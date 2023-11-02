def solution():
    # Calculate the total amount collected by Lily from selling the lottery tickets
    total_amount_collected = 5*(5+1)/2  # sum of first 5 integers starting from 1

    # Calculate the remaining amount after subtracting $4 profit
    remaining_amount = total_amount_collected - 4

    # Calculate the prize money for the winner
    prize_money = remaining_amount / 5

    result = prize_money
    return result

print(solution())