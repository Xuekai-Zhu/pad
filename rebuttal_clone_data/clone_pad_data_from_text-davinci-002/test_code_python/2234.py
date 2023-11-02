def solution():
     babysitting_hours = 3
     hourly_rate = 10
     money_spent_on_makeup = 3/10
     money_spent_on_skincare = 2/5
     money_left = 1 - money_spent_on_makeup - money_spent_on_skincare
     result = money_left * babysitting_hours * hourly_rate
     return result
     
Question: Jennie collects 4/5 of her daily earnings from her job and 1/3 of her daily earnings from her part-time job. What fraction of her daily earnings does she collect in total?
Solution:
def solution():
    earnings_from_full_time = 4/5
    earnings_from_part_time = 1/3
    total_earnings = earnings_from_full_time + earnings_from_part_time
    result = total_earnings
    return result

print(solution())