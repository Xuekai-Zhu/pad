def solution():
     total_potatoes = 6500
     damaged_potatoes = 150
     undamaged_potatoes = total_potatoes - damaged_potatoes
     Potato_bags = undamaged_potatoes / 50
     Potato_sale = Potato_bags * 72
     result = Potato_sale
     return result

print(solution())