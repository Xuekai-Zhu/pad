def solution():
     cleaning_time = 4
     cooking_time = 2
     working_time = 24 - (cleaning_time + cooking_time + 8)
     crafting_time = working_time / 2
     result = crafting_time
     return result

print(solution())