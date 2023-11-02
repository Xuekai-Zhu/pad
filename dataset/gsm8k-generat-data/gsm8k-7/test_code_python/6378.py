def solution():
    num_teeth_lost = 20 - 2 # Grant lost 20 teeth, but 2 were not put under his pillow
    total_money = 54 - 20 # Grant received $20 for his first tooth, so subtract that from the total

    # Calculate how much money Grant received per tooth after his first tooth
    money_per_tooth = total_money / num_teeth_lost
    result = money_per_tooth
    return result

print(solution())