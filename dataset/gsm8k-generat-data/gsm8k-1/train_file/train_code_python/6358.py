def solution():
    """Parker went to the gym and found 4 twenty pounds dumbbells set up for weightlifting. He added two more dumbbells to the setup and started his exercises. How many pounds of dumbbells is Parker using for his exercises?"""
    initial_dumbbells = 4
    added_dumbbells = 2
    weight_per_dumbbell = 20
    total_weight = (initial_dumbbells + added_dumbbells) * weight_per_dumbbell
    result = total_weight
    return result

print(solution())