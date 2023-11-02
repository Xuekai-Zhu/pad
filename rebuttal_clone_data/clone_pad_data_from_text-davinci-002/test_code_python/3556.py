def solution():
     June_savings = 21
     July_savings = 46
     August_savings = 45
     school_supplies = 12
     new_clothes = 54
     total_spent = school_supplies + new_clothes
     total_saved = June_savings + July_savings + August_savings
     aunt_gift = 25
     money_left = total_saved - total_spent + aunt_gift
     result = money_left
     return result

print(solution())