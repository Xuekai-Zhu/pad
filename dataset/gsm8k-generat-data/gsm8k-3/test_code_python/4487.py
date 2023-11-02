def solution():
    """Jean is trying to motivate herself to write her final paper. She eats one donut per 2 pages that she writes. If she writes 12 pages and each donut has 150 calories, how many calories does she eat?"""
    # Calculate the number of donuts Jean eats
    donuts_eaten = 12 // 2  # We use // to get the integer value of division

    # Calculate the total number of calories Jean eats
    total_calories = donuts_eaten * 150

    # Display the total number of calories Jean eats
    result = total_calories
    return result

print(solution())