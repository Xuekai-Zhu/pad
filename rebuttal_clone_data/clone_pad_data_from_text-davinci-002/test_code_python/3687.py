def solution():
     cartons_of_blueberries = 3
     number_of_blueberries_per_carton = 200
     total_number_of_blueberries = cartons_of_blueberries * number_of_blueberries_per_carton
     blueberries_per_muffin = 10
     total_number_of_muffins = total_number_of_blueberries / blueberries_per_muffin
     number_of_cinnamon_muffins = 60
     total_number_of_muffins_with_blueberries = total_number_of_muffins - number_of_cinnamon_muffins
     percentage_of_muffins_with_blueberries = total_number_of_muffins_with_blueberries / total_number_of_muffins * 100
     result = percentage_of_muffins_with_blueberries
     
     return result

print(solution())