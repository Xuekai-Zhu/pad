def solution():
    
    # Define the number of times the class meets per week and the duration of each meet
    meets_per_week = 4
    duration_per_meet = 2

    # Define the number of weeks the class meets
    weeks = 6

    # Calculate the total duration of the class meets
    total_duration = meets_per_week * duration_per_meet * weeks

    # Calculate the number of recipes that John learns
    recipes = total_duration // 1.5

    # Display the number of recipes
    result = recipes
    return result

print(solution())