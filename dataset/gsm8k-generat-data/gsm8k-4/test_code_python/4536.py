def solution():
    """Every Sunday John is allowed to watch cartoons. However, for every 10 minutes of cartoons, he has to do 8 minutes of chores. If he watches cartoons for 2 hours, how many minutes of chores does he have to do?"""
    # Define the time John is allowed to watch cartoons
    cartoon_time = 120

    # Calculate the time John has to spend on chores for every 10 minutes of cartoons
    chore_time = 8 / 10

    # Calculate the total time John has to spend on chores
    total_chore_time = (cartoon_time / 10) * chore_time

    # return the result
    result = total_chore_time
    return result

print(solution())