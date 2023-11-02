def solution():
    """It takes Jason 30 minutes to cut 1 lawn in his neighborhood. If he cuts 8 yards on both Saturday and Sunday, how many hours does he spend cutting grass?"""
    lawns_per_hour = 2
    lawns_per_day = 8
    days = 2
    total_lawns = lawns_per_day * days
    time_per_lawn = 30 / 60 # converting minutes to hours
    total_time = total_lawns * time_per_lawn
    result = total_time
    return result

print(solution())