def solution():
    
    # Define the number of Junebugs removed on Monday
    monday_junebugs = 39

    # Define the number of Junebugs removed on Tuesday and Wednesday
    tuesday_wednesday_junebugs = monday_junebugs * 2

    # Define the number of Junebugs removed on Thursday and Friday
    thursday_junebugs = 48
    friday_junebugs = 57

    # Calculate the total number of Junebugs removed
    total_junebugs = monday_junebugs + tuesday_wednesday_junebugs + thursday_junebugs + friday_junebugs

    # Calculate the average number of Junebugs removed per day
    average_junebugs = total_junebugs / 5

    # Display the average number of Junebugs removed per day
    result = average_junebugs
    return result

print(solution())