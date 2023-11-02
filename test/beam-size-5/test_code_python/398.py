def solution():
    
    flour_per_recipe = 3
    milk_per_recipe = 1
    flour_sold = 2
    milk_sold = 2
    flour_bottles_needed = flour_per_recipe - milk_sold
    flour_bags_needed = flour_sold / flour_per_recipe
    milk_bottles_needed = milk_sold / milk_per_recipe
    difference = flour_bags_needed - milk_bottles_needed
    result = difference
    return result

print(solution())