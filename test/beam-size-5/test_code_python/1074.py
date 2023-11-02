def solution():
    
    # Define the required number of toothpicks and the number of weeks it will take to save them
    required_toothpicks = 200
    weeks_to_save = 12

    # Define the number of toothpicks saved each week
    toothpicks_per_week = 10

    # Calculate the total number of toothpicks saved over 12 weeks
    total_saved = toothpicks_per_week * weeks_to_save

    # Calculate the number of remaining toothpicks to collect
    remaining_toothpicks = required_toothpicks - total_saved

    # Calculate the number of weeks it will take to collect the remaining toothpicks
    weeks_to_collect = remaining_toothpicks / toothpicks_per_week

    # Display the number of weeks it will take to collect the remaining toothpicks
    result = weeks_to_collect
    return result

print(solution())