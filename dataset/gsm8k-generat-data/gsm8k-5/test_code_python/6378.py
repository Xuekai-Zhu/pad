def solution():
    total_teeth = 20  # Grant lost 20 baby teeth
    teeth_lost = total_teeth - 2  # He lost 2 teeth in a different way
    total_money = 54  # Grant received a total of $54 from the tooth fairy
    initial_money = 20  # Grant received $20 for his first tooth
    money_left = total_money - initial_money  # The remaining money after the first tooth

    # Calculate the amount of money the tooth fairy left per tooth
    money_per_tooth = money_left / teeth_lost
    result = money_per_tooth
    return result

print(solution())