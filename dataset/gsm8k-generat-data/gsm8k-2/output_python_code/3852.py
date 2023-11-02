def solution():
    """Each slice of cheesecake contains 350 calories. If there are a total of 2800 calories in every cheesecake, and Kiley ate 25% of the cheesecake, how many slices of cheesecake did Kiley eat?"""
    cheesecake_calories = 2800
    slice_calories = 350
    total_slices = cheesecake_calories / slice_calories
    kiley_slices = total_slices * 0.25
    result = kiley_slices
    return result

print(solution())