def solution():
    
    donuts_per_page = 1/2
    pages_written = 12
    donuts_eaten = donuts_per_page * pages_written
    calories_per_donut = 150
    total_calories = donuts_eaten * calories_per_donut
    result = total_calories
    return result

print(solution())