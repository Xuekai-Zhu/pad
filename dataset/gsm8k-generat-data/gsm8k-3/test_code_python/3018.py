def solution():
    """Kara has to drink 4 ounces of water every time she takes her medication. Her medication instructions are to take one tablet three times a day. She followed the instructions for one week, but in the second week, she forgot twice on one day. How many ounces of water did she drink with her medication over those two weeks?"""
    # Define the amount of medication taken per day and the amount of water to drink with each dose
    MEDICATION_PER_DAY = 3
    WATER_PER_DOSE = 4

    # Calculate the total medication taken and water consumed in the first week
    medication_first_week = MEDICATION_PER_DAY * 7
    water_first_week = medication_first_week * WATER_PER_DOSE

    # Calculate the total medication taken and water consumed in the second week
    medication_second_week = (MEDICATION_PER_DAY * 6) + 2
    water_second_week = medication_second_week * WATER_PER_DOSE

    # Calculate the total water consumed over the two weeks
    total_water = water_first_week + water_second_week

    # Display the total water consumed
    result = total_water
    return result

print(solution())