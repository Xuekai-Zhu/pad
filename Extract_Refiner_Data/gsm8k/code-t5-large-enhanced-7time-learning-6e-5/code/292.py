def solution():
    
    # Define the amount of rice consumed per meal and per lunch and dinner
    RICE_PER_MEAL = 0.2
    RICE_PER_LUNCH_AND_DINNER = 0.2

    # Define the number of people in the household
    NUM_PEOPLE = 5

    # Define the total amount of rice in the household
    TOTAL_RICE = 42

    # Calculate the total amount of rice consumed per week
    RICE_PER_WEEK = RICE_PER_MEAL * NUM_PEOPLE * 2

    # Calculate the number of weeks the bag of rice will last
    weeks = TOTAL_RICE / RICE_PER_WEEK

    # Display the number of weeks
    result = weeks
    return result

print(solution())