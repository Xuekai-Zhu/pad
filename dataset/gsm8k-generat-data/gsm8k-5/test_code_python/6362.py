def solution():
    final_money = 360  # Frank had $360 left in his wallet
    remaining_money_after_magazine = final_money / (3/4)  # Frank spent 1/4 of the remaining money on a magazine
    remaining_money_after_groceries = remaining_money_after_magazine / (4/5)  # Frank spent 1/5 of his money on groceries
    initial_money = remaining_money_after_groceries  # This is the amount of money Frank had at first
    result = initial_money
    return result

print(solution())