def solution():
    cartoon_time = 120  # in minutes
    chore_ratio = 8 / 10  # 8 minutes of chores for 10 minutes of cartoons
    chores_time = (cartoon_time / 10) * chore_ratio
    result = chores_time
    return result

print(solution())