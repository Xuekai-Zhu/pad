def solution():
    """Matt needs to buy new plates for his home. He only wants to do dishes once a week. Three days a week it is only him and his son eating and they use 1 plate each. On the remainder of the days, his parents join them and everyone uses 2 plates that day. How many plates does he need to buy?"""
    days_one_plate = 3
    days_two_plates = 4
    plates_one_person = 1
    plates_two_people = 2
    
    total_plates = (days_one_plate * plates_one_person * 2) + (days_two_plates * plates_two_people * 2)
    
    result = total_plates
    return result

print(solution())