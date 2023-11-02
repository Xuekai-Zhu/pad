def solution():
    """Jason was told he could earn $3.00 for doing his laundry, $1.50 for cleaning his room, $0.75 for taking the trash to the curb each week and $0.50 for emptying the dishwasher. In a two week period, Jason emptied the dishwasher 6 times, did his laundry once, took the trash out twice and cleaned his room once. How much money did Jason earn?"""
    laundry_pay = 3
    room_pay = 1.5
    trash_pay = 0.75
    dishwasher_pay = 0.5
    total_laundry_pay = laundry_pay
    total_room_pay = room_pay
    total_trash_pay = trash_pay * 2
    total_dishwasher_pay = dishwasher_pay * 6
    total_pay = total_laundry_pay + total_room_pay + total_trash_pay + total_dishwasher_pay
    result = total_pay
    return result

print(solution())