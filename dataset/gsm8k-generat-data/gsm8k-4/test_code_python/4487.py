def solution():
    """Jean is trying to motivate herself to write her final paper. She eats one donut per 2 pages that she writes. If she writes 12 pages and each donut has 150 calories, how many calories does she eat?"""
    # Define the number of pages Jean writes and the number of donuts she eats
    pages_written = 12
    donuts_eaten = int(pages_written / 2)

    # Calculate the total number of calories Jean eats
    calories_per_donut = 150
    total_calories = donuts_eaten * calories_per_donut

    # Return the result
    return total_calories

print(solution())