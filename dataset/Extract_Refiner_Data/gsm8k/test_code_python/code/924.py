def solution():
    
    # Define the number of Junebugs removed on each day
    monday_removed = 39
    tuesday_removed = 2 * monday_removed
    wednesday_removed = 2 * monday_removed
    thursday_removed = 48
    friday_removed = 57

    # Calculate the total number of Junebugs removed
    total_removed = monday_removed + tuesday_removed + wednesday_removed + thursday_removed + friday_removed

    # Calculate the average number of Junebugs removed per day
    average_removed = total_removed / 3

    # Display the average number of Junebugs removed per day
    result = average_removed
    return result

print(solution())