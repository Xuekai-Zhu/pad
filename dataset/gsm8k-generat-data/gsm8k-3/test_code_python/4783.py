def solution():
    """Ryan is considering buying a new multivitamin brand.  Each pill has 50 mg of Vitamin A in it.  The recommended daily serving of Vitamin A is 200 mg.  How many pills does Ryan need to hit the recommended amount for the week?"""
    # Define the amount of Vitamin A per pill and the recommended daily serving
    VITAMIN_A_PER_PILL = 50
    DAILY_SERVING = 200

    # Calculate the number of pills needed for a daily serving
    pills_per_serving = DAILY_SERVING / VITAMIN_A_PER_PILL

    # Calculate the number of pills needed for a week's worth of servings
    pills_per_week = pills_per_serving * 7

    # Display the number of pills needed
    result = pills_per_week
    return result

print(solution())