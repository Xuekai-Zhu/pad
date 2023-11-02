def solution():
    initial_money = 400  # Gina had $400 initially
    mom_share = initial_money / 4  # Gina gave 1/4 of her money to her mom
    remaining_money = initial_money - mom_share  # Calculate the remaining money

    clothes_cost = initial_money / 8  # Gina spent 1/8 of her money on clothes
    remaining_money -= clothes_cost  # Calculate the remaining money again

    charity_share = initial_money / 5  # Gina gave 1/5 of her money to charity
    remaining_money -= charity_share  # Calculate the remaining money again

    result = remaining_money
    return result

print(solution())