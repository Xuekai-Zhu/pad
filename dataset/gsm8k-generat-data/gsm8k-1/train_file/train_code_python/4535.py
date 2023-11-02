def solution():
    """Every Sunday John is allowed to watch cartoons. However, for every 10 minutes of cartoons, he has to do 8 minutes of chores. If he watches cartoons for 2 hours, how many minutes of chores does he have to do?"""
    cartoons_time = 2 * 60 # 2 hours converted to minutes
    chore_ratio = 8 / 10 # for every 10 minutes of cartoons, he has to do 8 minutes of chores
    chore_time = cartoons_time // 10 * chore_ratio # divide by 10 to get the number of 10-minute cartoon intervals, then multiply by chore_ratio to get chore time
    result = chore_time
    return result

print(solution())