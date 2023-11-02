def solution():
    
    bread_bought = 200
    day_1_eaten = bread_bought * (1/4)
    remaining_bread_1 = bread_bought - day_1_eaten
    day_2_eaten = remaining_bread_1 * (2/5)
    remaining_bread_2 = remaining_bread_1 - day_2_eaten
    day_3_eaten = remaining_bread_2 * (1/2)
    remaining_bread_3 = remaining_bread_2 - day_3_eaten
    result = remaining_bread_3
    return result

print(solution())