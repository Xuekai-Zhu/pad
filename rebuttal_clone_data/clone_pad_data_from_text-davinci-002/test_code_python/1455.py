def solution():
    garden_one_total = 20
    garden_one_tomatoes = garden_one_total * .10
    garden_two_total = 15
    garden_two_tomatoes = garden_two_total * (1/3)
    total_tomatoes = garden_one_tomatoes + garden_two_tomatoes
    total_plants = garden_one_total + garden_two_total
    percent_tomatoes = total_tomatoes / total_plants
    result = percent_tomatoes
    
    return result

print(solution())