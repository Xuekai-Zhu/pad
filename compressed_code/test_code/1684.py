def solution():
    
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