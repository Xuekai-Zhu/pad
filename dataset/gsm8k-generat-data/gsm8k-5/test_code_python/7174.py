def solution():
    initial_money = 65  # Lulu has $65 in her piggy bank
    spent_on_ice_cream = 5  # Lulu spent $5 on ice cream
    remaining_money = initial_money - spent_on_ice_cream  # Lulu's remaining money after buying ice cream
    spent_on_tshirt = remaining_money / 2  # Lulu spent half of the remaining money on a t-shirt
    remaining_money -= spent_on_tshirt  # Lulu's remaining money after buying the t-shirt
    deposited_money = remaining_money / 5  # Lulu deposited a fifth of her remaining money in the bank
    remaining_money -= deposited_money  # Lulu's remaining money after depositing in the bank

    result = remaining_money
    return result

print(solution())