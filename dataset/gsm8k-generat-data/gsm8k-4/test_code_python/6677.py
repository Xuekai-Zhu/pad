def solution():
    """Justin needs to collect one flower for each classmate that is in his 2nd-grade class. It takes him on average 10 minutes to find a flower he likes. He has been gathering for 2 hours. Assuming he has lost 3 of the flowers he initially gathered, how many more minutes does he need to look if he has 30 classmates?"""
    # Define the number of classmates and the time Justin has been gathering flowers
    classmates = 30
    gathering_time = 2 * 60

    # Calculate the total time it takes Justin to find a flower and the number of flowers he needs
    flower_time = 10
    total_flowers = classmates - 3

    # Calculate the time Justin has already spent gathering flowers
    already_spent = total_flowers * flower_time

    # Calculate the remaining time Justin needs to gather flowers
    remaining_time = gathering_time - already_spent

    result = remaining_time
    return result

print(solution())