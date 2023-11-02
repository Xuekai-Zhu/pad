def solution():
    """A baker bakes 5 loaves of bread an hour in one oven. He has 4 ovens. From Monday to Friday, he bakes for 5 hours, but on Saturday and Sunday, he only bakes for 2 hours. How many loaves of bread does the baker bake in 3 weeks?"""
    # Define the number of loaves of bread the baker bakes per hour per oven
    LOAVES_PER_HOUR_PER_OVEN = 5

    # Define the number of ovens the baker has
    NUM_OVENS = 4

    # Define the number of hours the baker bakes each day
    MON_FRI_HOURS = 5
    SAT_SUN_HOURS = 2

    # Define the number of weeks
    NUM_WEEKS = 3

    # Calculate the total number of loaves of bread baked from Monday to Friday
    weekday_loaves = MON_FRI_HOURS * LOAVES_PER_HOUR_PER_OVEN * NUM_OVENS * 5

    # Calculate the total number of loaves of bread baked on Saturday and Sunday
    weekend_loaves = SAT_SUN_HOURS * LOAVES_PER_HOUR_PER_OVEN * NUM_OVENS * 2

    # Calculate the total number of loaves of bread baked over 3 weeks
    total_loaves = (weekday_loaves + weekend_loaves) * NUM_WEEKS

    # Display the total number of loaves baked
    result = total_loaves
    return result

print(solution())