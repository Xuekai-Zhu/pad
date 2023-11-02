def solution():
    # Calculate the total amount of money for the lost teeth
    lost_money = 20 + 0.5 * 20  # First tooth + half for the dropped tooth

    # Calculate how much money is left for the other teeth
    remaining_money = 54 - lost_money

    # Calculate the number of teeth that the remaining money is spread over
    num_teeth = 20 - 2  # Subtract the lost teeth

    # Calculate the average money per tooth
    money_per_tooth = remaining_money / num_teeth
    result = money_per_tooth
    return result

print(solution())