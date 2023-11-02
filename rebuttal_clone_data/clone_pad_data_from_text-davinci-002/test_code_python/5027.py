def solution():
     cans_from_home = 12
     cans_from_ grandparents = cans_from_home * 3
     cans_from_neighbor = 46
     cans_from_dad = 250
     total_cans = cans_from_home + cans_from_grandparents + cans_from_neighbor + cans_from_dad
     total_money = total_cans * 0.25
     money_to_save = total_money / 2
     result = money_to_save
     return result

print(solution())