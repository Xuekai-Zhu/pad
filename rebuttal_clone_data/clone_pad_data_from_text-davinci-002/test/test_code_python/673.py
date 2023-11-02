def solution():
     cat_food_bags = 2
     cat_food_weight = 3
     dog_food_bags = 2
     dog_food_weight = cat_food_weight + 2
     ounces_per_pound = 16
     total_cat_food_ounces = cat_food_bags * cat_food_weight * ounces_per_pound
     total_dog_food_ounces = dog_food_bags * dog_food_weight * ounces_per_pound
     total_pet_food_ounces = total_cat_food_ounces + total_dog_food_ounces
     result =  total_pet_food_ounces
 
     return result

print(solution())