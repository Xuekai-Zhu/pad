def solution():
     starting_dogs = 30
     starting_cats = 28
     starting_lizards = 20
     monthly_adoptions_dogs = starting_dogs * 0.50
     monthly_adoptions_cats = starting_cats * 0.25
     monthly_adoptions_lizards = starting_lizards * 0.20
     monthly_new_pets = 13
     total_monthly_adoptions = monthly_adoptions_dogs + monthly_adoptions_cats + monthly_adoptions_lizards
     ending_dogs = starting_dogs - monthly_adoptions_dogs + monthly_new_pets
     ending_cats = starting_cats - monthly_adoptions_cats + monthly_new_pets
     ending_lizards = starting_lizards - monthly_adoptions_lizards + monthly_new_pets
     total_pets_after_one_month = ending_dogs + ending_cats + ending_lizards
     result = total_pets_after_one_month
     return result

print(solution())