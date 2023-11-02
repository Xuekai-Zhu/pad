def solution():
    """A baker bakes 5 loaves of bread an hour in one oven. He has 4 ovens. From Monday to Friday, he bakes for 5 hours, but on Saturday and Sunday, he only bakes for 2 hours. How many loaves of bread does the baker bake in 3 weeks?"""
    # Define the number of loaves of bread baked per oven per hour and the number of ovens
    loaves_per_hour_per_oven = 5
    num_ovens = 4

    # Define the number of hours baked per day
    hours_per_day = [5, 5, 5, 5, 5, 2, 2]

    # Calculate the total number of loaves baked per day and per week
    loaves_per_day = loaves_per_hour_per_oven * num_ovens * hours_per_day
    loaves_per_week = sum(loaves_per_day)

    # Calculate the total number of loaves baked in 3 weeks
    loaves_for_3_weeks = loaves_per_week * 3

    result = loaves_for_3_weeks
    return result

print(solution())