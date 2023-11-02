def solution():
    """Matt needs to buy new plates for his home. He only wants to do dishes once a week. Three days a week it is only him and his son eating and they use 1 plate each. On the remainder of the days, his parents join them and everyone uses 2 plates that day. How many plates does he need to buy?"""
    days_with_3_people = 4 # 7 days in a week - 3 days with only Matt and his son
    plates_per_day_with_3_people = 2 # 2 plates per person
    plates_per_day_with_2_people = 2 # 2 plates per person
    days_with_2_people = 7 - days_with_3_people
    total_plates = (days_with_3_people * plates_per_day_with_3_people * 3) + (days_with_2_people * plates_per_day_with_2_people * 4)
    result = total_plates
    return result

print(solution())