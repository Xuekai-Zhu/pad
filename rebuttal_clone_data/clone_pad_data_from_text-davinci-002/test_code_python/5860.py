def solution():
     repair_fee = 10
     corner_light = 2 * repair_fee
     brake_disk = 3 * corner_light
     total_spent = repair_fee + corner_light + (2 * brake_disk)
     post_repair_savings = 480
     result = post_repair_savings + total_spent
     return result

print(solution())