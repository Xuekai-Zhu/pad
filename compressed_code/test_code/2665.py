def solution():
    
    samantha_sleeps = 8
    baby_sleeps = 2.5 * samantha_sleeps
    father_sleeps_per_baby_hour = 0.5
    father_sleeps_per_day = father_sleeps_per_baby_hour * baby_sleeps
    father_sleeps_per_week = father_sleeps_per_day * 7
    result = father_sleeps_per_week
    return result

print(solution())