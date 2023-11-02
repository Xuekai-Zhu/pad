def solution():
    """James won a money prize at a charity raffle. He donated half of his winnings back to the charity, then spent $2 on a hot dog to celebrate his win. He had $55 left over. How many dollars did he win?"""
    remaining_money = 55
    hot_dog_cost = 2
    money_spent = remaining_money + hot_dog_cost
    donated_money = money_spent / 2
    total_money = remaining_money + donated_money
    result = total_money
    return result

print(solution())