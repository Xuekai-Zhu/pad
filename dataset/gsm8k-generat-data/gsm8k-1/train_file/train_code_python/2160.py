def solution():
    """On Saturday morning, Renata had $10 to spend. She first went and made a $4 donation in exchange for a ticket to the local charity draw. When the draw was done, she was declared the winner of the 5th prize of $90. Excited, she quickly dashed to play slots at one of the casinos in Atlantic City. Unfortunately, she lost $50 at the first slot machine, $10 at the second and $5 at the last one. Dejected, she decided to take a long walk. She soon grew thirsty and entered the first gas station she saw. She picked a $1 bottle of water and while paying for it, she bought a $1 lottery ticket. To her utter delight, she won an instant prize of $65. How much money did Renata end up having?"""
    starting_money = 10
    charity_donation = 4
    charity_prize = 90
    slot_loss_1 = 50
    slot_loss_2 = 10
    slot_loss_3 = 5
    water_purchase = 1
    lottery_purchase = 1
    lottery_prize = 65

    # calculate total expenses
    total_expenses = (
        charity_donation
        + slot_loss_1
        + slot_loss_2
        + slot_loss_3
        + water_purchase
        + lottery_purchase
    )

    # calculate total winnings
    total_winnings = charity_prize + lottery_prize

    # calculate final amount of money
    final_money = starting_money + total_winnings - total_expenses

    # return result
    return final_money

print(solution())