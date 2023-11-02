def solution():
    cecil_money = 600  # Cecil has $600
    catherine_money = (2*cecil_money) - 250  # Catherine has $250 less than twice as much as Cecil
    carmela_money = (2*cecil_money) + 50  # Carmela has $50 more than twice Cecil's money

    # Calculate the total money they have altogether
    total_money = cecil_money + catherine_money + carmela_money
    result = total_money
    return result

print(solution())