def solution():
    """Each slice of cheesecake contains 350 calories.  If there are a total of 2800 calories in every cheesecake, and Kiley ate 25% of the cheesecake, how many slices of cheesecake did Kiley eat?"""
    # Define the number of calories per cheesecake and the percentage Kiley ate
    CALORIES_PER_CHEESECAKE = 2800
    PERCENTAGE_EATEN = 0.25

    # Calculate the number of calories Kiley ate
    calories_eaten = CALORIES_PER_CHEESECAKE * PERCENTAGE_EATEN

    # Calculate the number of slices of cheesecake Kiley ate
    slices_eaten = calories_eaten / 350

    # Display the number of slices of cheesecake Kiley ate
    result = slices_eaten
    return result

print(solution())