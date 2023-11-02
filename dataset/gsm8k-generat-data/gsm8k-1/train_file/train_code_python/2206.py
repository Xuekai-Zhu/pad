def solution():
    """The football coach makes his players run up and down the bleachers 40 times. Each time they run up and down 32 stairs one way. If each stair burns 2 calories, how many calories does each player burn during this exercise?"""
    runs = 40
    stairs_per_run = 32 * 2  # up and down
    calories_per_stair = 2
    total_calories = runs * stairs_per_run * calories_per_stair
    result = total_calories
    return result

print(solution())