def solution():
    # Define the time it takes for each activity
    commute_time = 30
    grocery_time = 30
    dry_cleaning_time = 10
    dog_grooming_time = 20
    dinner_time = 90

    # Add up the total time for all activities
    total_time = commute_time + grocery_time + dry_cleaning_time + dog_grooming_time + dinner_time

    # Convert total time to hours and minutes
    hours = total_time // 60
    minutes = total_time % 60

    # Add the time to 4:00 pm
    dinner_hour = 4 + hours
    dinner_minute = minutes

    # Adjust for 24-hour time
    if dinner_hour > 12:
        dinner_hour -= 12

    # Print the dinner time
    result = str(dinner_hour) + ":" + str(dinner_minute).zfill(2) + " pm"
    return result

print(solution())