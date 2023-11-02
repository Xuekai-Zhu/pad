def solution():
    donuts_per_page = 0.5
    pages_written = 12
    calories_per_donut = 150

    # Calculate the total number of donuts Jean will eat
    total_donuts = pages_written * donuts_per_page

    # Calculate the total number of calories Jean will consume from the donuts
    total_calories = total_donuts * calories_per_donut
    result = total_calories
    return result

print(solution())