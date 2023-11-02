def solution():
    money_left = 800  # Noemi still has $800 in her purse
    money_lost = 400 + 500  # Noemi lost $400 on roulette and $500 on blackjack
    money_begin = money_left + money_lost  # Calculate how much money Noemi began with
    result = money_begin
    return result

print(solution())