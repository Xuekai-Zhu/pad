def solution():
     total_cans = 85
     cans_picked_up_by_ladonna = 25
     cans_picked_up_by_prikya = cans_picked_up_by_ladonna * 2
     cans_picked_up_by_yoki = total_cans - (cans_picked_up_by_ladonna + cans_picked_up_by_prikya)
     result = cans_picked_up_by_yoki
     return result

print(solution())