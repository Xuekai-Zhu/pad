def solution():
    """Max was doing homework in three different subjects. It took him 20 minutes to finish tasks from biology and two times more time to finish history. Geography took him the most time, three times more than history. How much time did Max spend on doing his homework?"""
    bio_time = 20
    history_time = bio_time * 2
    geo_time = history_time * 3
    total_time = bio_time + history_time + geo_time
    result = total_time
    return result

print(solution())