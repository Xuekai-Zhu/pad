def solution():
    eggplants_per_day = 12
    carrots_per_day = 9
    potatoes_per_day = 8
    days_per_week = 4

    # Calculate the total number of vegetables Conor can chop in a week
    total_eggs = eggplants_per_day * days_per_week
    total_carrots = carrots_per_day * days_per_week
    total_potatoes = potatoes_per_day * days_per_week

    # Calculate the total number of vegetables Conor can chop
    total_vegetables = total_eggs + total_carrots + total_potatoes
    result = total_vegetables
    return result

print(solution())