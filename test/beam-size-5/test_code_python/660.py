def solution():
    
    class_meets_per_week = 4
    class_hours_per_class = 2
    weeks = 6
    total_class_hours = class_meets_per_week * class_hours_per_class * weeks
    recipe_time_per_recipe = 1.5
    recipes_ learned = total_class_hours // recipe_time_per_recipe
    result = recipes_learned
    return result

print(solution())