def solution():
    
    starting_marbles = 40
    breakfast_loss = 3
    lunch_gift = 5
    afternoon_gain = 12
    susie_gift = lunch_gift * 2

    remaining_marbles = starting_marbles - breakfast_loss - lunch_gift + afternoon_gain + susie_gift
    result = remaining_marbles
    return result

print(solution())