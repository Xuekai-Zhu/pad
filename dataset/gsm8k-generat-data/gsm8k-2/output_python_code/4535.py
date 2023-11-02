def solution():
    """Every Sunday John is allowed to watch cartoons. However, for every 10 minutes of cartoons, he has to do 8 minutes of chores. If he watches cartoons for 2 hours, how many minutes of chores does he have to do?"""
    cartoons_time = 120  # in minutes
    cartoon_chore_ratio = 10/8
    chores_time = cartoons_time // cartoon_chore_ratio
    result = chores_time
    return result

print(solution())