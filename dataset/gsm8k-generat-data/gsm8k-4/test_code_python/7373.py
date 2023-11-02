def solution():
    """Hank reads the newspaper every morning, 5 days a week for 30 minutes. He reads part of a novel every evening, 5 days a week, for 1 hour. He doubles his reading time on Saturday and Sundays. How many minutes does Hank spend reading in 1 week?"""
    # Define the time spent reading the newspaper
    newspaper_time = 5 * 30

    # Define the time spent reading the novel
    novel_time = 5 * 60

    # Define the time spent reading on weekends
    weekend_time = (2 * newspaper_time) + (2 * novel_time)

    # Define the total time spent reading in a week
    total_time = newspaper_time + novel_time + weekend_time

    result = total_time
    return result

print(solution())