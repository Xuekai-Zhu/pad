def solution():
    """Ryan is considering buying a new multivitamin brand. Each pill has 50 mg of Vitamin A in it. The recommended daily serving of Vitamin A is 200 mg. How many pills does Ryan need to hit the recommended amount for the week?"""
    # Define the recommended daily serving and the number of days in a week
    recommended_daily_serving = 200
    days_in_week = 7

    # Calculate the total recommended serving for the week
    recommended_weekly_serving = recommended_daily_serving * days_in_week

    # Calculate the number of pills Ryan needs to reach the recommended weekly serving
    pills_needed = recommended_weekly_serving / 50

    # Round up to the nearest whole number of pills
    pills_needed = round(pills_needed)

    # return the result
    result = pills_needed
    return result

print(solution())