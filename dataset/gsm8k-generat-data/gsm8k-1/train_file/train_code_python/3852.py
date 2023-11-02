def solution():
    """Each slice of cheesecake contains 350 calories. If there are a total of 2800 calories in every cheesecake, and Kiley ate 25% of the cheesecake, how many slices of cheesecake did Kiley eat?"""
    total_calories = 2800
    calories_per_slice = 350
    eaten_percent = 0.25
    eaten_calories = total_calories * eaten_percent
    slices_eaten = eaten_calories / calories_per_slice
    result = slices_eaten
    return result

print(solution())