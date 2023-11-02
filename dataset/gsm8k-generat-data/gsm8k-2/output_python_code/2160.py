def solution():
    """On Saturday morning, Renata had $10 to spend. She first went and made a $4 donation in exchange for a ticket to the local charity draw. When the draw was done, she was declared the winner of the 5th prize of $90. Excited, she quickly dashed to play slots at one of the casinos in Atlantic City. Unfortunately, she lost $50 at the first slot machine, $10 at the second and $5 at the last one. Dejected, she decided to take a long walk. She soon grew thirsty and entered the first gas station she saw. She picked a $1 bottle of water and while paying for it, she bought a $1 lottery ticket. To her utter delight, she won an instant prize of $65. How much money did Renata end up having?"""
    starting_money = 10
    donation = 4
    charity_prize = 90
    first_slot_loss = 50
    second_slot_loss = 10
    third_slot_loss = 5
    bottle_of_water = 1
    lottery_ticket = 1
    lottery_prize = 65

    total_spent = donation + first_slot_loss + second_slot_loss + third_slot_loss + bottle_of_water + lottery_ticket
    total_won = charity_prize + lottery_prize
    final_money = starting_money - total_spent + total_won
    result = final_money
    return result

print(solution())