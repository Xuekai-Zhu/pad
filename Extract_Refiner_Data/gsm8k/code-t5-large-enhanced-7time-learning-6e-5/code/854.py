def solution():
    
    # Define the number of people infected per day
    PEOPLE_PER_DAY = 10 + 6

    # Calculate the total number of people infected after three days
    total_people = PEOPLE_PER_DAY * 3

    # Display the total number of people infected
    result = total_people
    return result

print(solution())