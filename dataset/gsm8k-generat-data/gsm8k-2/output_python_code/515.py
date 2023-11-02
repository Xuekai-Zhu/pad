def solution():
    """Max was doing homework in three different subjects. It took him 20 minutes to finish tasks from biology and two times more time to finish history. Geography took him the most time, three times more than history. How much time did Max spend on doing his homework?"""
    bio_time = 20
    hist_time = 2 * bio_time
    geo_time = 3 * hist_time
    total_time = bio_time + hist_time + geo_time
    result = total_time
    return result

print(solution())