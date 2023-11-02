def solution():
    """Justin needs to collect one flower for each classmate that is in his 2nd-grade class. It takes him on average 10 minutes to find a flower he likes. He has been gathering for 2 hours. Assuming he has lost 3 of the flowers he initially gathered, how many more minutes does he need to look if he has 30 classmates?"""
    # Define the number of classmates and the time it takes to find a flower
    classmates = 30
    time_per_flower = 10 # in minutes

    # Calculate the total time it will take to collect all the flowers, in minutes
    total_time = classmates * time_per_flower

    # Subtract the time Justin has already spent and the time lost to lost flowers
    remaining_time = total_time - (2 * 60) - (3 * time_per_flower)

    # Display the remaining time in minutes
    result = remaining_time
    return result

print(solution())