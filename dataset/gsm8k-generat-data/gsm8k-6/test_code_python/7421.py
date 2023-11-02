def solution():
    # Calculate the amount of money the first winner will receive
    first_winner = 2400/3  

    # Calculate the remaining amount of money after the first winner is awarded
    remaining_money = 2400 - first_winner  

    # Calculate the amount of money each of the next ten winners will receive
    next_ten_winners = remaining_money/10  

    result = next_ten_winners
    return result

print(solution())