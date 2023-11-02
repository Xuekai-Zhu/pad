def solution():
    pages_written = 12  # Jean writes 12 pages
    donuts_eaten = pages_written / 2  # She eats 1 donut per 2 pages
    calories_per_donut = 150  # Each donut has 150 calories

    # Calculate the total number of calories Jean eats
    total_calories = donuts_eaten * calories_per_donut
    result = total_calories
    return result

print(solution())