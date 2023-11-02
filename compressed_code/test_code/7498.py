def solution():
    
    starting_money = 10
    charity_donation = 4
    charity_prize = 90
    slot_loss_1 = 50
    slot_loss_2 = 10
    slot_loss_3 = 5
    water_purchase = 1
    lottery_purchase = 1
    lottery_prize = 65

    
    total_expenses = (
        charity_donation
        + slot_loss_1
        + slot_loss_2
        + slot_loss_3
        + water_purchase
        + lottery_purchase
    )

    
    total_winnings = charity_prize + lottery_prize

    
    final_money = starting_money + total_winnings - total_expenses

    
    return final_money

print(solution())