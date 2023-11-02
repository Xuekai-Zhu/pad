def solution():
    
    # Define the number of people and letters per week
    num_people = 5
    num_letters_per_week = 2

    # Define the number of pages per letter
    num_pages_per_letter = 5

    # Calculate the total number of pages per week
    total_pages_per_week = num_people * num_letters_per_week

    # Calculate the total number of pages per week
    total_pages_per_week = total_pages_per_week * num_pages_per_letter

    # Calculate the total time spent writing per week
    time_per_week = total_pages_per_week / 6

    # Convert the time to hours
    hours_per_week = time_per_week / 60

    # Return the result
    result = hours_per_week
    return result

print(solution())