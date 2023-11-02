def solution():
    """Alex has not washed his clothes for a month; 18 shirts, 12 pants, 17 sweaters, and 13 jeans are waiting to be washed. Alex's washing machine can wash a maximum of 15 items per cycle. Each cycle takes 45 minutes. How many hours will it take the washing machine to wash all the clothes?"""

    total_clothes = 18 + 12 + 17 + 13
    items_per_cycle = 15
    cycles_needed = total_clothes // items_per_cycle
    if total_clothes % items_per_cycle != 0:
        cycles_needed += 1
    time_per_cycle = 45/60 #convert 45 minutes into hours
    total_time = cycles_needed * time_per_cycle
    result = total_time
    return result

print(solution())