def solution():
    """Jean is trying to motivate herself to write her final paper. She eats one donut per 2 pages that she writes. If she writes 12 pages and each donut has 150 calories, how many calories does she eat?"""
    donuts_per_page = 1/2
    pages_written = 12
    donuts_eaten = donuts_per_page * pages_written
    calories_per_donut = 150
    total_calories = donuts_eaten * calories_per_donut
    result = total_calories
    return result

print(solution())