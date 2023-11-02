def solution():
    """Each slice of cheesecake contains 350 calories. If there are a total of 2800 calories in every cheesecake, and Kiley ate 25% of the cheesecake, how many slices of cheesecake did Kiley eat?"""
    # Define the number of calories per cheesecake and the percentage Kiley ate
    CALORIES_PER_CHEESECAKE = 2800
    KILEY_PERCENTAGE = 0.25

    # Calculate the total number of calories Kiley ate
    kiley_calories = CALORIES_PER_CHEESECAKE * KILEY_PERCENTAGE

    # Calculate the number of slices Kiley ate, assuming each slice contains 350 calories
    kiley_slices = kiley_calories / 350

    # Round the result to the nearest integer
    result = round(kiley_slices)

    return result

print(solution())