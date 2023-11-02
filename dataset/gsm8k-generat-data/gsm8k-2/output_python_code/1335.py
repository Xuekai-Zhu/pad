def solution():
    """It takes Jason 30 minutes to cut 1 lawn in his neighborhood. If he cuts 8 yards on both Saturday and Sunday, how many hours does he spend cutting grass?"""
    time_per_lawn = 0.5 # 30 minutes = 0.5 hours
    num_lawns = 8
    total_lawn_time = num_lawns * 2 * time_per_lawn # 8 yards on both Saturday and Sunday
    result = total_lawn_time
    return result

print(solution())